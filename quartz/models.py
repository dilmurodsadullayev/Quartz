from django.db import models
import os
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext_lazy as _

def photo_directory_path(instance, filename):
    photo_id = instance.id or 'temp'
    return os.path.join('photo', str(photo_id), filename)

def video_directory_path(instance, filename):
    video_id = instance.id or 'temp'
    return os.path.join('video', str(video_id), filename)


def news_image_directory_path(instance, filename):
    photo_id = instance.id or 'temp'
    return os.path.join('news_image', str(photo_id), filename)

def activity_image_directory_path(instance, filename):
    photo_id = instance.id or 'temp'
    return os.path.join('activity_image', str(photo_id), filename)


class Photo(models.Model):
    title = models.CharField(max_length=30)
    photo = models.ImageField(upload_to=photo_directory_path)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=30)
    video = models.FileField(upload_to=video_directory_path)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        try:
            return f"{self.title} | {self.video.url}"
        except ValueError:
            return f"{self.title} | [Video not uploaded]"


class News(models.Model):
    title = models.CharField(max_length=150)
    cover_image = models.ImageField(upload_to=news_image_directory_path)
    description = models.TextField()
    content = RichTextUploadingField()  # Bu yerda editor ishlaydi
    created_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title[:30]


class Activity(models.Model):
    title = models.CharField(max_length=150)
    cover_image = models.ImageField(upload_to=activity_image_directory_path)
    description = models.TextField()
    content = RichTextUploadingField()  # Bu yerda editor ishlaydi
    created_at = models.DateTimeField(auto_now_add=True)


class Meeting(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    location = models.CharField(max_length=200)
    meeting_date = models.DateTimeField()
    content = RichTextUploadingField()  # Bu yerda editor ishlaydi
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title


class Tender(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    content = RichTextUploadingField()  # Bu yerda editor ishlaydi
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Feedback(models.Model):
    name = models.CharField(_("Ism"), max_length=100)
    phone = models.CharField(_("Telefon raqam"), max_length=20)
    subject = models.CharField(_("Sarlavha"), max_length=255)
    message = models.TextField(_("Xabar matni"))
    created_at = models.DateTimeField(_("Yuborilgan vaqti"), auto_now_add=True)

    def __str__(self):
        return f"{self.subject} ({self.name})"

    class Meta:
        verbose_name = _("Murojaat")
        verbose_name_plural = _("Murojaatlar")
        ordering = ['-created_at']






