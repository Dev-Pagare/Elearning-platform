from django.db import models
import os

class SystemAdmin(models.Model):
    name = models.CharField(max_length=30, default="System Admin")
    number = models.IntegerField()
    email = models.EmailField(max_length=50)
    address = models.TextField(max_length=50)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=16)

    def __str__(self):
        return self.name


class Course(models.Model):
    category_choices = [
        ('marketing','Marketing'),('programming','Programming'),
        ('web','Web Development'),('app','App Development'),
        ('game','Game Development'),('database','Database Management'),
        ('network','Network Security'),('cloud','Cloud Computing'),
        ('iot','Internet of Things'),('blockchain','Blockchain'),
        ('cyber','Cyber Security'),('vr','Virtual Reality'),
        ('ar','Augmented Reality'),('robotics','Robotics'),
        ('bigdata','Big Data'),('datascience','Data Science'),
        ('ai','Artificial Intelligence'),('ml','Machine Learning'),
        ('dl','Deep Learning'),('cv','Computer Vision'),
        ('nlp','NLP'),('videoedit','Video Editing'),
    ]
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=category_choices)
    description = models.TextField(max_length=20000, blank=True)
    is_active = models.BooleanField(default=True)
    image_url = models.FileField(upload_to='courses/', default='courses/default.jpg', blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

    def save(self, *args, **kwargs):
        if self.pk:
            try:
                old = Course.objects.get(pk=self.pk)
                if old.image_url and self.image_url:
                    if old.image_url.name != self.image_url.name:
                        if old.image_url.name != 'courses/default.jpg':
                            if os.path.isfile(old.image_url.path):
                                os.remove(old.image_url.path)
            except (Course.DoesNotExist, ValueError, OSError):
                pass
        super(Course, self).save(*args, **kwargs)

    def __str__(self):
        return self.course_name


class Chapter(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='chapters')
    title = models.CharField(max_length=200)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.course.course_name} — {self.title}"


class Lesson(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    code_example = models.TextField(blank=True, help_text="Code example for this lesson")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.chapter.title} — {self.title}"


class Student(models.Model):
    name = models.CharField(max_length=30, default="Student")
    number = models.IntegerField(blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True)
    address = models.TextField(max_length=50, blank=True)
    username = models.CharField(max_length=20, unique=True, default="student")
    password = models.CharField(max_length=16, blank=True)
    enrolled_courses = models.ManyToManyField(Course, related_name='Student', blank=True)

    def __str__(self):
        return self.name


class CourseRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    request_id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_requests')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='course_requests')
    request_date = models.DateField(auto_now=True)
    reason = models.TextField(max_length=500, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")

    class Meta:
        unique_together = ('course', 'student')

    def __str__(self):
        return f"{self.student.name} → {self.course.course_name} ({self.status})"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    admin_reply = models.TextField(blank=True, default='')
    is_replied = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} — {self.subject}"

    class Meta:
        ordering = ['-submitted_at']


class Quiz(models.Model):
    chapter = models.OneToOneField(Chapter, on_delete=models.CASCADE, related_name='quiz')
    title = models.CharField(max_length=200)
    pass_marks = models.IntegerField(default=60)

    def __str__(self):
        return f"Quiz: {self.chapter.title}"


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()
    option_a = models.CharField(max_length=300)
    option_b = models.CharField(max_length=300)
    option_c = models.CharField(max_length=300)
    option_d = models.CharField(max_length=300)
    correct_option = models.CharField(max_length=1, choices=[
        ('A','Option A'), ('B','Option B'),
        ('C','Option C'), ('D','Option D')
    ])
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.question_text[:60]


class QuizResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField()
    total = models.IntegerField()
    passed = models.BooleanField(default=False)
    attempted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-attempted_at']

    def __str__(self):
        return f"{self.student.name} - {self.quiz.title} - {self.score}/{self.total}"


class LessonProgress(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='lesson_progress')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='progress')
    completed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'lesson')

    def __str__(self):
        return f"{self.student.name} — {self.lesson.title}"


class Certificate(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='certificates')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='certificates')
    issued_at = models.DateTimeField(auto_now_add=True)
    certificate_id = models.CharField(max_length=20, unique=True)

    class Meta:
        unique_together = ('student', 'course')

    def __str__(self):
        return f"{self.student.name} — {self.course.course_name}"


class Notification(models.Model):
    NOTIF_TYPES = [
        ('approved',    'Course Approved'),
        ('rejected',    'Course Rejected'),
        ('certificate', 'Certificate Earned'),
        ('quiz_passed', 'Quiz Passed'),
        ('enrolled',    'Course Enrolled'),
    ]
    student    = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='notifications')
    notif_type = models.CharField(max_length=20, choices=NOTIF_TYPES)
    title      = models.CharField(max_length=200)
    message    = models.TextField()
    is_read    = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.student.name} — {self.title}"


class CourseReview(models.Model):
    course     = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews')
    student    = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='reviews')
    rating     = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # 1 to 5 stars
    review     = models.TextField(max_length=1000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('course', 'student')   # one review per student per course
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.student.name} → {self.course.course_name} ({self.rating}★)"