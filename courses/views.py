from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import (Course, Student, CourseRequest, Chapter, Lesson,
                     ContactMessage, Quiz, Question, QuizResult,
                     LessonProgress, Certificate, Notification, CourseReview,
                     SystemAdmin)
import json
import jwt
import uuid
from datetime import datetime, timedelta

_ADMIN_KEY = 'custom_admin_logged_in'

def _admin_required(view_fn):
    def wrapper(request, *args, **kwargs):
        if not request.session.get(_ADMIN_KEY):
            return redirect('/admin/login/')
        return view_fn(request, *args, **kwargs)
    wrapper.__name__ = view_fn.__name__
    return wrapper

def index(request):
    return render(request, 'index.html')

def contact_page(request):
    return render(request, 'contact.html')

def course_description_page(request):
    return render(request, 'course_description.html')

def login_page(request):
    return render(request, 'signin.html')

def forgot_password_page(request):
    return render(request, 'forgot_password.html')

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

def search_page(request):                          # ← NEW
    return render(request, 'search.html')

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
        reviews = CourseReview.objects.filter(course=course)
        total_r = reviews.count()
        avg_r   = round(sum(r.rating for r in reviews) / total_r, 1) if total_r else 0
        course_data.append({
            "course_id":      course.pk,
            "course_name":    course.course_name,
            "category":       course.category,
            "description":    course.description,
            "image_url":      request.build_absolute_uri(course.image_url.url),
            "price":          price,
            "avg_rating":     avg_r,
            "total_reviews":  total_r,
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
        reviews = CourseReview.objects.filter(course=course)
        total_r = reviews.count()
        avg_r   = round(sum(r.rating for r in reviews) / total_r, 1) if total_r else 0
        return JsonResponse({"course": {
            "course_id":     course.pk,
            "course_name":   course.course_name,
            "category":      course.category,
            "description":   course.description,
            "image_url":     request.build_absolute_uri(course.image_url.url),
            "price":         price,
            "avg_rating":    avg_r,
            "total_reviews": total_r,
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
            Notification.objects.create(
                student=student,
                notif_type='enrolled',
                title='Enrollment Request Submitted',
                message=f'Your request for "{course.course_name}" has been submitted. Please wait for admin approval.',
            )
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
            image = request.build_absolute_uri(c.image_url.url) if request else c.image_url.url
        except:
            image = ''
        try:
            price = float(c.price)
        except:
            price = 0.0
        courses.append({
            "course_id": c.pk, "course_name": c.course_name,
            "category": c.category, "image_url": image,
            "description": c.description, "price": price,
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
                        'id': lesson.id, 'title': lesson.title,
                        'content': lesson.content, 'code_example': lesson.code_example,
                    })
                chapters.append({'id': chapter.id, 'title': chapter.title, 'lessons': lessons})
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
            name=data.get('name'), email=data.get('email'),
            subject=data.get('subject'), message=data.get('message'),
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
            already_passed = QuizResult.objects.filter(student=student, quiz=quiz, passed=True).exists()
        except Student.DoesNotExist:
            pass

    questions = [{'id': q.id, 'text': q.question_text,
                  'options': {'A': q.option_a, 'B': q.option_b, 'C': q.option_c, 'D': q.option_d}}
                 for q in quiz.questions.all()]
    return JsonResponse({'has_quiz': True, 'quiz_id': quiz.id, 'title': quiz.title,
                         'pass_percentage': quiz.pass_marks, 'already_passed': already_passed,
                         'questions': questions})

@csrf_exempt
def submit_quiz(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            quiz    = Quiz.objects.get(id=data.get('quiz_id'))
            student = Student.objects.get(username=data.get('username'))
        except (Quiz.DoesNotExist, Student.DoesNotExist):
            return JsonResponse({'error': 'Invalid data'}, status=400)

        questions = quiz.questions.all()
        total = questions.count()
        score = 0
        results = []
        for q in questions:
            user_ans = data.get('answers', {}).get(str(q.id), '').upper()
            correct  = q.correct_option.upper()
            is_correct = user_ans == correct
            if is_correct: score += 1
            results.append({'question': q.question_text, 'your_answer': user_ans,
                            'correct_answer': correct, 'is_correct': is_correct,
                            'options': {'A': q.option_a, 'B': q.option_b, 'C': q.option_c, 'D': q.option_d}})

        percentage = int((score / total) * 100) if total > 0 else 0
        passed = percentage >= quiz.pass_marks
        QuizResult.objects.create(student=student, quiz=quiz, score=score, total=total, passed=passed)

        if passed:
            Notification.objects.create(student=student, notif_type='quiz_passed',
                title='Quiz Passed! 🎉',
                message=f'You passed "{quiz.title}" with {percentage}% ({score}/{total} correct).')

        return JsonResponse({'score': score, 'total': total, 'percentage': percentage,
                             'passed': passed, 'pass_percentage': quiz.pass_marks, 'results': results})

@csrf_exempt
def mark_lesson_complete(request):
    if request.method == 'POST':
        try:
            data      = json.loads(request.body)
            username  = data.get('username')
            if not username:
                return JsonResponse({'error': 'Username missing'}, status=400)
            student = Student.objects.get(username=username)
            lesson  = Lesson.objects.get(id=data.get('lesson_id'))
            course  = Course.objects.get(pk=data.get('course_id'))
            LessonProgress.objects.get_or_create(student=student, lesson=lesson)
            total_lessons   = Lesson.objects.filter(chapter__course=course).count()
            completed       = LessonProgress.objects.filter(student=student, lesson__chapter__course=course).count()
            percentage      = int((completed / total_lessons) * 100) if total_lessons > 0 else 0
            course_complete = (completed == total_lessons)
            cert_id = None
            if course_complete:
                cert, created = Certificate.objects.get_or_create(
                    student=student, course=course,
                    defaults={'certificate_id': 'CERT-' + uuid.uuid4().hex[:10].upper()})
                cert_id = cert.certificate_id
                if created:
                    Notification.objects.create(student=student, notif_type='certificate',
                        title='Certificate Earned! 🏆',
                        message=f'Congratulations! You completed "{course.course_name}" and earned a certificate.')
            return JsonResponse({'status': 'ok', 'completed': completed, 'total': total_lessons,
                                 'percentage': percentage, 'course_complete': course_complete,
                                 'certificate_id': cert_id})
        except Student.DoesNotExist:
            return JsonResponse({'error': 'Student not found'}, status=400)
        except Lesson.DoesNotExist:
            return JsonResponse({'error': 'Lesson not found'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def get_progress(request):
    try:
        student       = Student.objects.get(username=request.GET.get('username'))
        course        = Course.objects.get(pk=request.GET.get('course_id'))
        total_lessons = Lesson.objects.filter(chapter__course=course).count()
        completed_ids = list(LessonProgress.objects.filter(student=student, lesson__chapter__course=course)
                             .values_list('lesson_id', flat=True))
        percentage = int((len(completed_ids) / total_lessons) * 100) if total_lessons > 0 else 0
        cert = Certificate.objects.filter(student=student, course=course).first()
        return JsonResponse({'completed_lesson_ids': completed_ids, 'total': total_lessons,
                             'percentage': percentage, 'certificate_id': cert.certificate_id if cert else None})
    except Exception:
        return JsonResponse({'completed_lesson_ids': [], 'total': 0, 'percentage': 0, 'certificate_id': None})

@csrf_exempt
def get_certificate(request):
    try:
        cert = Certificate.objects.get(certificate_id=request.GET.get('cert_id'))
        return JsonResponse({'status': 'ok', 'student_name': cert.student.name,
                             'course_name': cert.course.course_name,
                             'certificate_id': cert.certificate_id,
                             'issued_at': cert.issued_at.strftime('%B %d, %Y')})
    except Certificate.DoesNotExist:
        return JsonResponse({'status': 'error'}, status=404)

def get_dashboard(request):
    try:
        student  = Student.objects.get(username=request.GET.get('username'))
        enrolled = student.enrolled_courses.all()
        courses_data = []
        for course in enrolled:
            total_lessons = Lesson.objects.filter(chapter__course=course).count()
            completed     = LessonProgress.objects.filter(student=student, lesson__chapter__course=course).count()
            percentage    = int((completed / total_lessons) * 100) if total_lessons > 0 else 0
            cert = Certificate.objects.filter(student=student, course=course).first()
            try: image = course.image_url.url
            except: image = ''
            courses_data.append({'course_id': course.pk, 'course_name': course.course_name,
                                  'category': course.category, 'image_url': image,
                                  'total_lessons': total_lessons, 'completed_lessons': completed,
                                  'percentage': percentage,
                                  'certificate_id': cert.certificate_id if cert else None})
        recent_quizzes = QuizResult.objects.filter(student=student).order_by('-attempted_at')[:5]
        return JsonResponse({
            'student_name': student.name,
            'stats': {
                'total_enrolled':      enrolled.count(),
                'total_completed':     sum(1 for c in courses_data if c['percentage'] == 100),
                'total_certificates':  Certificate.objects.filter(student=student).count(),
                'total_quizzes_passed': QuizResult.objects.filter(student=student, passed=True).count(),
                'total_lessons_done':  LessonProgress.objects.filter(student=student).count(),
            },
            'courses': courses_data,
            'recent_quizzes': [{'quiz_title': qr.quiz.title, 'score': qr.score, 'total': qr.total,
                                 'percentage': int((qr.score/qr.total)*100) if qr.total else 0,
                                 'passed': qr.passed, 'attempted_at': qr.attempted_at.strftime('%b %d, %Y')}
                                for qr in recent_quizzes],
        })
    except Student.DoesNotExist:
        return JsonResponse({'error': 'Student not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def get_notifications(request):
    try:
        student = Student.objects.get(username=request.GET.get('username'))
        notifs  = Notification.objects.filter(student=student)[:20]
        unread  = Notification.objects.filter(student=student, is_read=False).count()
        return JsonResponse({'notifications': [{'id': n.id, 'type': n.notif_type, 'title': n.title,
                                                 'message': n.message, 'is_read': n.is_read,
                                                 'created_at': n.created_at.strftime('%b %d, %Y %I:%M %p')}
                                                for n in notifs], 'unread_count': unread})
    except Student.DoesNotExist:
        return JsonResponse({'notifications': [], 'unread_count': 0})

@csrf_exempt
def mark_notifications_read(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            student = Student.objects.get(username=data.get('username'))
            Notification.objects.filter(student=student, is_read=False).update(is_read=True)
            return JsonResponse({'status': 'ok'})
        except Student.DoesNotExist:
            return JsonResponse({'status': 'error'}, status=400)


def get_reviews(request):
    course_id = request.GET.get('course_id')
    username  = request.GET.get('username', '')
    try:
        course  = Course.objects.get(pk=course_id)
        reviews = CourseReview.objects.filter(course=course)
        total   = reviews.count()
        avg     = round(sum(r.rating for r in reviews) / total, 1) if total else 0
        breakdown = {i: reviews.filter(rating=i).count() for i in range(1, 6)}

        my_review  = None
        can_review = False
        if username:
            try:
                student    = Student.objects.get(username=username)
                can_review = student.enrolled_courses.filter(pk=course_id).exists()
                mine       = reviews.filter(student=student).first()
                if mine:
                    my_review = {'rating': mine.rating, 'review': mine.review}
            except Student.DoesNotExist:
                pass

        return JsonResponse({
            'avg_rating':  avg,
            'total':       total,
            'breakdown':   breakdown,
            'reviews': [{
                'id':         r.id,
                'student':    r.student.name,
                'rating':     r.rating,
                'review':     r.review,
                'created_at': r.created_at.strftime('%b %d, %Y'),
                'is_mine':    r.student.username == username,
            } for r in reviews],
            'my_review':  my_review,
            'can_review': can_review,
        })
    except Course.DoesNotExist:
        return JsonResponse({'avg_rating': 0, 'total': 0, 'breakdown': {},
                             'reviews': [], 'my_review': None, 'can_review': False})

@csrf_exempt
def submit_review(request):
    if request.method == 'POST':
        try:
            data      = json.loads(request.body)
            username  = data.get('username')
            course_id = data.get('course_id')
            rating    = int(data.get('rating', 0))
            review    = data.get('review', '').strip()

            if not username or not course_id or not (1 <= rating <= 5):
                return JsonResponse({'error': 'Invalid data'}, status=400)

            student = Student.objects.get(username=username)
            course  = Course.objects.get(pk=course_id)

            if not student.enrolled_courses.filter(pk=course_id).exists():
                return JsonResponse({'error': 'Not enrolled'}, status=403)

            obj, created = CourseReview.objects.update_or_create(
                course=course, student=student,
                defaults={'rating': rating, 'review': review})

            all_reviews = CourseReview.objects.filter(course=course)
            total = all_reviews.count()
            avg   = round(sum(r.rating for r in all_reviews) / total, 1) if total else 0

            return JsonResponse({'status': 'ok', 'created': created,
                                 'avg_rating': avg, 'total': total})
        except Student.DoesNotExist:
            return JsonResponse({'error': 'Student not found'}, status=400)
        except Course.DoesNotExist:
            return JsonResponse({'error': 'Course not found'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt
def forgot_password_verify(request):
    """Step 1: verify username + email match."""
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email    = request.POST.get('email', '').strip().lower()
        try:
            student = Student.objects.get(username=username)
            if student.email.strip().lower() == email:
                return JsonResponse({'status': 'success'})
            return JsonResponse({'status': 'error', 'message': 'Email does not match our records.'})
        except Student.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Username not found.'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request.'}, status=400)


@csrf_exempt
def forgot_password_reset(request):
    """Step 2: update the password."""
    if request.method == 'POST':
        username     = request.POST.get('username', '').strip()
        new_password = request.POST.get('new_password', '').strip()
        if not username or not new_password:
            return JsonResponse({'status': 'error', 'message': 'Missing fields.'})
        if len(new_password) < 6:
            return JsonResponse({'status': 'error', 'message': 'Password too short.'})
        try:
            student          = Student.objects.get(username=username)
            student.password = new_password
            student.save()
            return JsonResponse({'status': 'success'})
        except Student.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'User not found.'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request.'}, status=400)


def reply_contact_message(request, pk):
    """Renders the admin reply page for a specific contact message."""
    try:
        msg = ContactMessage.objects.get(pk=pk)
    except ContactMessage.DoesNotExist:
        from django.http import Http404
        raise Http404
    if request.method == 'POST':
        reply_text = request.POST.get('reply_text', '').strip()
        if reply_text:
            msg.admin_reply = reply_text
            msg.is_replied = True
            msg.is_read = True
            msg.save()
            return JsonResponse({'status': 'ok'})
        return JsonResponse({'status': 'error', 'message': 'Reply cannot be empty.'}, status=400)
    return render(request, 'admin_reply.html', {'msg': msg})


def admin_login_view(request):
    """Custom admin login using SystemAdmin model."""
    if request.session.get(_ADMIN_KEY):
        return redirect('/admin/')
    error = None
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        try:
            admin_obj = SystemAdmin.objects.get(username=username, password=password)
            request.session[_ADMIN_KEY] = True
            request.session['custom_admin_name'] = admin_obj.name
            request.session['custom_admin_id']   = admin_obj.pk
            return redirect('/admin/')
        except SystemAdmin.DoesNotExist:
            error = 'Invalid username or password.'
    return render(request, 'admin_login.html', {'error': error})


def admin_logout_view(request):
    """Clear admin session and redirect to login."""
    request.session.flush()
    return redirect('/admin/login/')


@_admin_required
def admin_home_view(request):
    """Main custom admin panel — passes all data for every section."""
    context = {
        'total_students':   Student.objects.count(),
        'active_courses':   Course.objects.filter(is_active=True).count(),
        'total_quizzes':    QuizResult.objects.count(),
        'unread_messages':  ContactMessage.objects.filter(is_read=False).count(),
        'total_enrollments': CourseRequest.objects.filter(status='approved').count(),
        'courses':          Course.objects.all().order_by('-pk'),
        'students':         Student.objects.prefetch_related('enrolled_courses').order_by('-pk'),
        'quiz_results':     QuizResult.objects.select_related('student', 'quiz').order_by('-attempted_at')[:50],
        'contact_messages': ContactMessage.objects.order_by('-submitted_at'),
        'pending_requests': CourseRequest.objects.filter(status='pending').select_related('student', 'course'),
        'category_choices': Course.category_choices,
        'admin_name': request.session.get('custom_admin_name', 'Admin'),
    }
    return render(request, 'admin_panel.html', context)


@_admin_required
@csrf_exempt
def admin_add_course(request):
    """Add a new course via the custom admin panel."""
    if request.method == 'POST':
        try:
            course = Course(
                course_name=request.POST.get('course_name', '').strip(),
                category=request.POST.get('category', ''),
                description=request.POST.get('description', '').strip(),
                price=request.POST.get('price', 0),
                is_active=request.POST.get('is_active') == 'true',
            )
            if request.FILES.get('image'):
                course.image_url = request.FILES['image']
            course.save()
            return JsonResponse({'status': 'ok', 'course_id': course.pk,
                                  'course_name': course.course_name})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'message': 'POST required'}, status=405)


@_admin_required
@csrf_exempt
def admin_delete_course(request, pk):
    """Delete a course."""
    if request.method == 'POST':
        try:
            Course.objects.get(pk=pk).delete()
            return JsonResponse({'status': 'ok'})
        except Course.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Not found'}, status=404)
    return JsonResponse({'status': 'error'}, status=405)


@_admin_required
@csrf_exempt
def admin_toggle_course(request, pk):
    """Toggle course active/inactive status."""
    if request.method == 'POST':
        try:
            course = Course.objects.get(pk=pk)
            course.is_active = not course.is_active
            course.save()
            return JsonResponse({'status': 'ok', 'is_active': course.is_active})
        except Course.DoesNotExist:
            return JsonResponse({'status': 'error'}, status=404)
    return JsonResponse({'status': 'error'}, status=405)


@_admin_required
@csrf_exempt
def admin_approve_request(request, pk):
    """Approve a course enrollment request."""
    if request.method == 'POST':
        try:
            req = CourseRequest.objects.get(pk=pk)
            req.status = 'approved'
            req.save()
            req.student.enrolled_courses.add(req.course)
            Notification.objects.create(
                student=req.student, notif_type='approved',
                title='Enrollment Approved! 🎉',
                message=f'Your request for "{req.course.course_name}" has been approved.',
            )
            return JsonResponse({'status': 'ok'})
        except CourseRequest.DoesNotExist:
            return JsonResponse({'status': 'error'}, status=404)
    return JsonResponse({'status': 'error'}, status=405)


@_admin_required
@csrf_exempt
def admin_reject_request(request, pk):
    """Reject a course enrollment request."""
    if request.method == 'POST':
        try:
            req = CourseRequest.objects.get(pk=pk)
            req.status = 'rejected'
            req.save()
            Notification.objects.create(
                student=req.student, notif_type='rejected',
                title='Enrollment Rejected',
                message=f'Your request for "{req.course.course_name}" was not approved.',
            )
            return JsonResponse({'status': 'ok'})
        except CourseRequest.DoesNotExist:
            return JsonResponse({'status': 'error'}, status=404)
    return JsonResponse({'status': 'error'}, status=405)


@_admin_required
@csrf_exempt
def admin_mark_msg_read(request, pk):
    """Mark a contact message as read."""
    if request.method == 'POST':
        try:
            msg = ContactMessage.objects.get(pk=pk)
            msg.is_read = True
            msg.save()
            return JsonResponse({'status': 'ok'})
        except ContactMessage.DoesNotExist:
            return JsonResponse({'status': 'error'}, status=404)
    return JsonResponse({'status': 'error'}, status=405)