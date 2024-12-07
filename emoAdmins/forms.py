from django import forms
from emoAdmins.models import Assignment,Question

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ["title", "file"]  # Match the fields in the model


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["title", "body"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter your question title",
                }
            ),
            "body": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Provide detailed context for your question",
                    "rows": 5,
                }
            ),
        }
