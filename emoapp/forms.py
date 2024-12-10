from django import forms
from emoapp.models import S_Assignment, SurveyResponse


class SubmitForm(forms.ModelForm):
    class Meta:
        model = S_Assignment
        fields = ["title", "file"]


class SurveyResponseForm(forms.ModelForm):
    class Meta:
        model = SurveyResponse
        fields = ["response_text"]
        widgets = {
            "response_text": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Write your answer here...",
                    "rows": 3,
                    "style": "border-color: #198754;",
                }
            ),
        }
