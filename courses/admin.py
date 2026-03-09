from django.contrib import admin
from .models import SystemAdmin, Course, Student, CourseRequest, Chapter, Lesson, ContactMessage, Quiz, Question, QuizResult


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 1


class ChapterInline(admin.StackedInline):
    model = Chapter
    extra = 1


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'category', 'price', 'is_active')
    list_filter = ('category', 'is_active')
    search_fields = ('course_name',)
    inlines = [ChapterInline]


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'order')
    inlines = [LessonInline]


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'chapter', 'order')


@admin.register(CourseRequest)
class CourseRequestAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'status', 'request_date')
    list_filter = ('status',)
    actions = ['approve_requests', 'reject_requests']

    def approve_requests(self, request, queryset):
        for req in queryset:
            req.status = 'approved'
            req.save()
            req.student.enrolled_courses.add(req.course)
        self.message_user(request, f"{queryset.count()} request(s) approved!")
    approve_requests.short_description = "✅ Approve selected requests"

    def reject_requests(self, request, queryset):
        queryset.update(status='rejected')
        self.message_user(request, f"{queryset.count()} request(s) rejected!")
    reject_requests.short_description = "❌ Reject selected requests"


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'username', 'email', 'number')
    search_fields = ('name', 'username', 'email')


@admin.register(SystemAdmin)
class SystemAdminAdmin(admin.ModelAdmin):
    list_display = ('name', 'username', 'email')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'submitted_at', 'is_read')
    list_filter = ('is_read',)
    search_fields = ('name', 'email', 'subject')
    readonly_fields = ('name', 'email', 'subject', 'message', 'submitted_at')
    actions = ['mark_as_read']

    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
        self.message_user(request, "Messages marked as read!")
    mark_as_read.short_description = "✅ Mark as Read"


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'chapter', 'pass_marks')
    inlines = [QuestionInline]


@admin.register(QuizResult)
class QuizResultAdmin(admin.ModelAdmin):
    list_display = ('student', 'quiz', 'score', 'total', 'passed', 'attempted_at')
    list_filter = ('passed',)
    readonly_fields = ('student', 'quiz', 'score', 'total', 'passed', 'attempted_at')
    