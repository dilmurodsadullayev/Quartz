# your_app_name/translation.py

from modeltranslation.translator import translator, TranslationOptions
from .models import Photo, Video, News, Activity, Meeting, Tender

# 1. Photo modeli uchun tarjima sozlamalari
class PhotoTranslationOptions(TranslationOptions):
    fields = ('title',)  # Qaysi maydonni tarjima qilish kerakligi

# 2. Video modeli uchun tarjima sozlamalari
class VideoTranslationOptions(TranslationOptions):
    fields = ('title',)

# 3. News modeli uchun tarjima sozlamalari
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'content')

# 4. Activity modeli uchun tarjima sozlamalari
class ActivityTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'content')

# 5. Meeting modeli uchun tarjima sozlamalari
class MeetingTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'location', 'content')

# 6. Tender modeli uchun tarjima sozlamalari
class TenderTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'content')


# BARCHA MODELLARNI RO'YXATDAN O'TKAZISH:
translator.register(Photo, PhotoTranslationOptions)
translator.register(Video, VideoTranslationOptions)
translator.register(News, NewsTranslationOptions)
translator.register(Activity, ActivityTranslationOptions)
translator.register(Meeting, MeetingTranslationOptions)
translator.register(Tender, TenderTranslationOptions)