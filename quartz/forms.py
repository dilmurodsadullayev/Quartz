# feedback/forms.py
import re  # Regular Expression modulini import qilamiz
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'phone', 'subject', 'message']

    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        # Barcha maydonlar uchun HTML 'required' atributini qo'shish
        for field in self.fields:
            self.fields[field].widget.attrs['required'] = True

        # Har bir maydonga alohida sozlamalar
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': _('Ismingiz'),
        })
        self.fields['phone'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': _('+998XXYYYYYYY'),
        })
        self.fields['subject'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': _('Sarlavha'),
        })
        self.fields['message'].widget.attrs.update({
            'class': 'form-control',
            'rows': '7',
            'placeholder': _('Xabar matni...'),
        })

    # Telefon raqamini validatsiya qilish uchun maxsus metod
    def clean_phone(self):
        phone_number = self.cleaned_data.get('phone')

        # O'zbekiston telefon raqamlari uchun RegEx
        # Format: +998 va undan keyin 9 ta raqam
        phone_pattern = re.compile(r'^\+998\d{9}$')

        if not phone_pattern.match(phone_number):
            # Agar format mos kelmasa, xatolik xabarini chiqarish
            raise ValidationError(
                _("Telefon raqami noto'g'ri formatda. Iltimos, +998XXXXXXXXX formatida kiriting."),
                code='invalid_phone_number'
            )

        return phone_number