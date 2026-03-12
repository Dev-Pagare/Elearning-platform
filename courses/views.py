from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import Course, Student, CourseRequest, Chapter, Lesson, ContactMessage, Quiz, Question, QuizResult, LessonProgress, Certificate
import json
import jwt
import uuid
from datetime import datetime, timedelta

def index(request):
    return render(request, 'index.html')

def contact_page(request):
    return render(request, 'contact.html')

def course_description_page(request):
    return render(request, 'course_description.html')

def login_page(request):
    return render(request, 'signin.html')

def signup_page(request):
    return render(request, 'register.html')

def profile_page(request):
    return render(request, 'profile.html')

def request_page(request):
    return render(request, 'req.html')

def enrolled_courses_page(request):
    return render(request, 'enrolled_courses.html')

def learn_page(request):
    return render(request, 'learn.html')

def dashboard_page(request):
    return render(request, 'dashboard.html')

def generate_token(username):
    payload = {"username": username, "exp": datetime.utcnow() + timedelta(days=1)}
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
    if isinstance(token, bytes):
        token = token.decode('utf-8')
    return token

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = Student.objects.filter(username=username, password=password)
        if user.exists():
            return JsonResponse({"status": "success", "token": generate_token(username)})
        return JsonResponse({"status": "invalid username or password"})

def signup(request):
    if request.method == 'POST':
        try:
            name = request.POST['name']
            number = request.POST['number']
            email = request.POST['email']
            address = request.POST['address']
            username = request.POST['username']
            password = request.POST['password']
            if Student.objects.filter(username=username).exists():
                return JsonResponse({"status": "student already exists"})
            Student(name=name, number=number, email=email, address=address, username=username, password=password).save()
            return JsonResponse({"status": "success", "token": generate_token(username)})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})

def all_courses(request):
    courses = Course.objects.filter(is_active=True)
    course_data = []
    for course in courses:
        try:
            price = float(course.price)
        except AttributeError:
            price = 0.0
        course_data.append({
            "course_id": course.pk,
            "course_name": course.course_name,
            "category": course.category,
            "description": course.description,
            "image_url": request.build_absolute_uri(course.image_url.url),
            "price": price,
        })
    return JsonResponse({"courses": course_data})

def get_course(request):
    if request.method == 'GET':
        course_id = request.GET['course_id']
        course = Course.objects.get(pk=course_id)
        try:
            price = float(course.price)
        except AttributeError:
            price = 0.0
        return JsonResponse({"course": {
            "course_id": course.pk,
            "course_name": course.course_name,
            "category": course.category,
            "description": course.description,
            "image_url": request.build_absolute_uri(course.image_url.url),
            "price": price,
        }})

def student_info(request):
    if request.method == 'POST':
        try:
            token = request.headers.get('Authorization').split(" ")[1]
            username = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])["username"]
            student = Student.objects.get(username=username)
            student_data = json.loads(serializers.serialize('json', [student]))[0]['fields']
            return JsonResponse({"student": student_data, "enrolled_courses": get_enrolled_courses(username, request)})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=401)

def creat_course_request(request):
    if request.method == 'POST':
        try:
            course_id = request.POST['course_id']
            reason = request.POST['reason']
            token = request.headers.get('Authorization').split(" ")[1]
            username = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])["username"]
            student = Student.objects.get(username=username)
            course = Course.objects.get(pk=course_id)
            if CourseRequest.objects.filter(course=course, student=student).exists():
                return JsonResponse({"status": "request already exists"})
            CourseRequest.objects.create(course=course, student=student, reason=reason)
            return JsonResponse({"status": "success"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})

def get_course_request(request):
    course_requests = CourseRequest.objects.filter(student_id=1)
    return JsonResponse({"course_requests": list(course_requests.values())})

def get_enrolled_courses(username, request=None):
    student = Student.objects.get(username=username)
    courses = []
    for c in student.enrolled_courses.all():
        try:
            if request:
                image = request.build_absolute_uri(c.image_url.url)
            else:
                image = c.image_url.url if c.image_url else ''
        except:
            image = ''
        try:
            price = float(c.price)
        except:
            price = 0.0
        courses.append({
            "course_id": c.pk,
            "course_name": c.course_name,
            "category": c.category,
            "image_url": image,
            "description": c.description,
            "price": price,
        })
    return courses

def get_course_content(request):
    if request.method == 'GET':
        course_id = request.GET.get('course_id')
        try:
            course = Course.objects.get(pk=course_id)
            chapters = []
            for chapter in course.chapters.all():
                lessons = []
                for lesson in chapter.lessons.all():
                    lessons.append({
                        'id': lesson.id,
                        'title': lesson.title,
                        'content': lesson.content,
                        'code_example': lesson.code_example,
                    })
                chapters.append({
                    'id': chapter.id,
                    'title': chapter.title,
                    'lessons': lessons,
                })
            return JsonResponse({'chapters': chapters})
        except Course.DoesNotExist:
            return JsonResponse({'error': 'Course not found'}, status=404)

def check_access(request):
    if request.method == 'POST':
        try:
            course_id = request.POST.get('course_id')
            token = request.headers.get('Authorization').split(" ")[1]
            username = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])["username"]
            student = Student.objects.get(username=username)
            course = Course.objects.get(pk=course_id)
            has_access = student.enrolled_courses.filter(pk=course_id).exists()
            req = CourseRequest.objects.filter(course=course, student=student).first()
            status = req.status if req else 'none'
            return JsonResponse({'has_access': has_access, 'status': status})
        except Exception as e:
            return JsonResponse({'has_access': False, 'status': 'none'})

def save_contact(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        ContactMessage.objects.create(
            name=data.get('name'),
            email=data.get('email'),
            subject=data.get('subject'),
            message=data.get('message'),
        )
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'}, status=400)

def get_quiz(request):
    chapter_id = request.GET.get('chapter_id')
    username = request.GET.get('username')
    try:
        chapter = Chapter.objects.get(id=chapter_id)
        quiz = chapter.quiz
    except (Chapter.DoesNotExist, Quiz.DoesNotExist):
        return JsonResponse({'has_quiz': False})

    already_passed = False
    if username:
        try:
            student = Student.objects.get(username=username)
            already_passed = QuizResult.objects.filter(
                student=student, quiz=quiz, passed=True
            ).exists()
        except Student.DoesNotExist:
            pass

    questions = []
    for q in quiz.questions.all():
        questions.append({
            'id': q.id,
            'text': q.question_text,
            'options': {
                'A': q.option_a,
                'B': q.option_b,
                'C': q.option_c,
                'D': q.option_d,
            }
        })

    return JsonResponse({
        'has_quiz': True,
        'quiz_id': quiz.id,
        'title': quiz.title,
        'pass_percentage': quiz.pass_marks,
        'already_passed': already_passed,
        'questions': questions
    })

@csrf_exempt
def submit_quiz(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        quiz_id = data.get('quiz_id')
        username = data.get('username')
        answers = data.get('answers', {})

        try:
            quiz = Quiz.objects.get(id=quiz_id)
            student = Student.objects.get(username=username)
        except (Quiz.DoesNotExist, Student.DoesNotExist):
            return JsonResponse({'error': 'Invalid data'}, status=400)

        questions = quiz.questions.all()
        total = questions.count()
        score = 0
        results = []

        for q in questions:
            user_ans = answers.get(str(q.id), '').upper()
            correct = q.correct_option.upper()
            is_correct = user_ans == correct
            if is_correct:
                score += 1
            results.append({
                'question': q.question_text,
                'your_answer': user_ans,
                'correct_answer': correct,
                'is_correct': is_correct,
                'options': {
                    'A': q.option_a, 'B': q.option_b,
                    'C': q.option_c, 'D': q.option_d
                }
            })

        percentage = int((score / total) * 100) if total > 0 else 0
        passed = percentage >= quiz.pass_marks

        QuizResult.objects.create(
            student=student, quiz=quiz,
            score=score, total=total, passed=passed
        )

        return JsonResponse({
            'score': score,
            'total': total,
            'percentage': percentage,
            'passed': passed,
            'pass_percentage': quiz.pass_marks,
            'results': results
        })

@csrf_exempt
def mark_lesson_complete(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            lesson_id = data.get('lesson_id')
            course_id = data.get('course_id')

            if not username:
                return JsonResponse({'error': 'Username missing'}, status=400)

            student = Student.objects.get(username=username)
            lesson = Lesson.objects.get(id=lesson_id)
            course = Course.objects.get(pk=course_id)

            LessonProgress.objects.get_or_create(student=student, lesson=lesson)

            total_lessons = Lesson.objects.filter(chapter__course=course).count()
            completed = LessonProgress.objects.filter(
                student=student, lesson__chapter__course=course
            ).count()

            percentage = int((completed / total_lessons) * 100) if total_lessons > 0 else 0
            course_complete = (completed == total_lessons)

            cert_id = None
            if course_complete:
                cert, created = Certificate.objects.get_or_create(
                    student=student,
                    course=course,
                    defaults={'certificate_id': 'CERT-' + uuid.uuid4().hex[:10].upper()}
                )
                cert_id = cert.certificate_id

            return JsonResponse({
                'status': 'ok',
                'completed': completed,
                'total': total_lessons,
                'percentage': percentage,
                'course_complete': course_complete,
                'certificate_id': cert_id,
            })
        except Student.DoesNotExist:
            return JsonResponse({'error': 'Student not found'}, status=400)
        except Lesson.DoesNotExist:
            return JsonResponse({'error': 'Lesson not found'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def get_progress(request):
    username = request.GET.get('username')
    course_id = request.GET.get('course_id')
    try:
        student = Student.objects.get(username=username)
        course = Course.objects.get(pk=course_id)
        total_lessons = Lesson.objects.filter(chapter__course=course).count()
        completed_ids = list(
            LessonProgress.objects.filter(
                student=student, lesson__chapter__course=course
            ).values_list('lesson_id', flat=True)
        )
        percentage = int((len(completed_ids) / total_lessons) * 100) if total_lessons > 0 else 0
        cert = Certificate.objects.filter(student=student, course=course).first()
        return JsonResponse({
            'completed_lesson_ids': completed_ids,
            'total': total_lessons,
            'percentage': percentage,
            'certificate_id': cert.certificate_id if cert else None,
        })
    except Exception as e:
        return JsonResponse({'completed_lesson_ids': [], 'total': 0, 'percentage': 0, 'certificate_id': None})

@csrf_exempt
def get_certificate(request):
    cert_id = request.GET.get('cert_id')
    try:
        cert = Certificate.objects.get(certificate_id=cert_id)
        return JsonResponse({
            'status': 'ok',
            'student_name': cert.student.name,
            'course_name': cert.course.course_name,
            'certificate_id': cert.certificate_id,
            'issued_at': cert.issued_at.strftime('%B %d, %Y'),
        })
    except Certificate.DoesNotExist:
        return JsonResponse({'status': 'error'}, status=404)

def get_dashboard(request):
    username = request.GET.get('username')
    try:
        student = Student.objects.get(username=username)

        # Enrolled courses + progress
        enrolled = student.enrolled_courses.all()
        courses_data = []
        for course in enrolled:
            total_lessons = Lesson.objects.filter(chapter__course=course).count()
            completed = LessonProgress.objects.filter(
                student=student, lesson__chapter__course=course
            ).count()
            percentage = int((completed / total_lessons) * 100) if total_lessons > 0 else 0
            cert = Certificate.objects.filter(student=student, course=course).first()
            try:
                image = course.image_url.url
            except:
                image = ''
            courses_data.append({
                'course_id': course.pk,
                'course_name': course.course_name,
                'category': course.category,
                'image_url': image,
                'total_lessons': total_lessons,
                'completed_lessons': completed,
                'percentage': percentage,
                'certificate_id': cert.certificate_id if cert else None,
            })

        # Stats
        total_enrolled = enrolled.count()
        total_completed = sum(1 for c in courses_data if c['percentage'] == 100)
        total_certificates = Certificate.objects.filter(student=student).count()
        total_quizzes_passed = QuizResult.objects.filter(student=student, passed=True).count()
        total_lessons_done = LessonProgress.objects.filter(student=student).count()

        # Recent quiz results
        recent_quizzes = QuizResult.objects.filter(student=student).order_by('-attempted_at')[:5]
        quiz_data = []
        for qr in recent_quizzes:
            quiz_data.append({
                'quiz_title': qr.quiz.title,
                'score': qr.score,
                'total': qr.total,
                'percentage': int((qr.score / qr.total) * 100) if qr.total > 0 else 0,
                'passed': qr.passed,
                'attempted_at': qr.attempted_at.strftime('%b %d, %Y'),
            })

        return JsonResponse({
            'student_name': student.name,
            'stats': {
                'total_enrolled': total_enrolled,
                'total_completed': total_completed,
                'total_certificates': total_certificates,
                'total_quizzes_passed': total_quizzes_passed,
                'total_lessons_done': total_lessons_done,
            },
            'courses': courses_data,
            'recent_quizzes': quiz_data,
        })
    except Student.DoesNotExist:
        return JsonResponse({'error': 'Student not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)