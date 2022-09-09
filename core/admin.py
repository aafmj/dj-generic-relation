from django.contrib import admin
from django.contrib.admin import register

from .models import *
from django.contrib.contenttypes.admin import GenericTabularInline

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Question)
# admin.site.register(Answer)
admin.site.register(Activity)


class AnswerTabularInline(GenericTabularInline):
    model = Activity


@register(Answer)
class Answer(admin.ModelAdmin):
    inlines = [AnswerTabularInline]
