# your_app_name/admin.py

from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from .models import Photo, Video, News, Activity, Meeting, Tender, Feedback

# Har bir model uchun TabbedTranslationAdmin'dan meros olamiz
@admin.register(Photo)
class PhotoAdmin(TabbedTranslationAdmin):
    list_display = ('title', 'created_at')

@admin.register(Video)
class VideoAdmin(TabbedTranslationAdmin):
    list_display = ('title', 'created_at')

@admin.register(News)
class NewsAdmin(TabbedTranslationAdmin):
    list_display = ('title', 'created_at')

@admin.register(Activity)
class ActivityAdmin(TabbedTranslationAdmin):
    list_display = ('title', 'created_at')

@admin.register(Meeting)
class MeetingAdmin(TabbedTranslationAdmin):
    list_display = ('title', 'location', 'meeting_date')

@admin.register(Tender)
class TenderAdmin(TabbedTranslationAdmin):
    list_display = ('title', 'start_time', 'end_time')



@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('subject', 'name', 'phone', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'phone', 'subject', 'message')
    readonly_fields = ('name', 'phone', 'subject', 'message', 'created_at')