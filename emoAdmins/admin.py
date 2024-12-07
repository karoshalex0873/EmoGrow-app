from django.contrib import admin
from emoAdmins.models import Question, teacher, Assignment

# Register your models here.
admin.site.register(teacher)
admin.site.register(Assignment)
admin.site.register(Question)