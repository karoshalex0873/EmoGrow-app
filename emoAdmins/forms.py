from django import forms
from emoAdmins.models import Assignment
class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ["title", "file"]  # Match the fields in the model
