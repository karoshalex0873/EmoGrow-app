# Generated by Django 5.1.3 on 2024-12-04 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emoAdmins', '0002_notice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='email',
            new_name='Email',
        ),
    ]