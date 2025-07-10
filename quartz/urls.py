from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('set_language/<str:language_code>/',views.set_language, name='set_language'),
    path('project', views.project_view, name='project'),
    path('news', views.news_view, name='news'),
    path('news/<int:news_id>/detail', views.news_detail_view, name='news_detail'),
    path('activities', views.activity_view, name='activity'),
    path('activity/<int:activity_id>/detail', views.activity_detail_view, name='activity_detail'),
    path('meeting', views.meeting_view, name='meeting'),
    path('meeting/<int:meeting_id>/detail', views.meeting_detail_view, name='meeting_detail'),
    path('tender', views.tender_view, name='tender'),
    path('tender/<int:tender_id>/detail', views.tender_detail_view, name='tender_detail'),
    path('partners', views.partners_view, name='partners'),
    path('feedback', views.feedback_view, name='feedback'),
    path('training', views.training_view, name='training'),
]