from django import forms
from emoAdmins.models import Assignment,Question

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ["title", "file"]  # Match the fields in the model


class QuestionsForm(forms.ModelForm):
    class Meta:
        model = Question
        fields=["title","body"]
