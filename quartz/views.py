from django.shortcuts import get_object_or_404, redirect, render
from .models import News, Activity, Tender, Meeting
from django.contrib import messages
from .forms import FeedbackForm
from django.utils.translation import gettext as _
from languages import en
from languages import uz

# Create your views here.

def set_language(request, language_code):
    # Tilni sessiyada saqlash
    request.session['language'] = language_code
    # Foydalanuvchini avvalgi sahifaga yoki asosiy sahifaga qaytarish
    return redirect(request.META.get('HTTP_REFERER', '/'))


def index_view(request):
    news = News.objects.order_by('-created_at')[:3]
    tenders = Tender.objects.order_by('-created_at')[:3]
    # news_one = News.objects.get(id=1)
    # meeting_one = Meeting.objects.get(id=2)

    language = request.session.get('language', 'en')

    # Tarjimalarni tanlash
    if language == 'uz':
        translations = uz.index.translations
    else:
        translations = en.index.translations
    ctx = {
        'news': news,
        'tenders': tenders,
        'translations': translations,
        # 'news_one': news_one,
        # 'meeting_one':meeting_one
    }
    return render(request, 'quartz/index.html', ctx)

def project_view(request):
    ctx = {

    }
    return render(request, 'quartz/project.html', ctx)


def news_view(request):
    news = News.objects.all().order_by('-created_at')
    ctx = {
        'news': news

    }
    return render(request, 'quartz/news.html', ctx)


def news_detail_view(request, news_id):
    new = get_object_or_404(News, pk=news_id)
    ctx = {
        'new': new

    }
    return render(request, 'quartz/news_detail.html', ctx)



def activity_view(request):
    activities = Activity.objects.all()

    ctx = {
        'activities': activities

    }
    return render(request, 'quartz/activity.html', ctx)


def activity_detail_view(request, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)

    ctx = {
        'activity': activity

    }
    return render(request, 'quartz/activity_detail.html', ctx)


def meeting_view(request):
    meetings = Meeting.objects.all()
    ctx = {
        'meetings': meetings
    }
    return render(request, 'quartz/meeting.html', ctx)

def meeting_detail_view(request, meeting_id):
    meeting = get_object_or_404(Meeting, pk=meeting_id)
    ctx = {
        'meeting': meeting

    }
    return render(request, 'quartz/meeting_detail.html', ctx)


def tender_view(request):
    tenders = Tender.objects.all()
    ctx = {
        'tenders': tenders
    }
    return render(request, 'quartz/tender.html', ctx)

def tender_detail_view(request, tender_id):
    tender = get_object_or_404(Tender, pk=tender_id)
    ctx = {
        'tender': tender

    }
    return render(request, 'quartz/tender_detail.html', ctx)

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _("Sizning murojaatingiz muvaffaqiyatli yuborildi. Adminga xabar berildi!"))
            return redirect('feedback')
    else:
        form = FeedbackForm()
    ctx = {
        'form': form
    }
    return render(request, 'quartz/feedback.html', ctx)


def partners_view(request):
    ctx = {

    }
    return render(request, 'quartz/partners.html', ctx)

def training_view(request):
    ctx = {

    }
    return render(request, 'quartz/training.html', ctx)




def custom_404(request, exception):
    return render(request, '404.html', status=404)