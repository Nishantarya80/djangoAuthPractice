from django.contrib import admin
from .models import Course, Instructor, Lesson

# Register your models here.
class LessonInline(admin.StackedInline):
    model = Lesson 
    extra = 1
class CourseAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'name', 'description']
    inlines = [LessonInline]

admin.site.register(Course,CourseAdmin)
admin.site.register(Instructor)