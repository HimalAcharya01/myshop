# Generated by Django 5.1 on 2024-08-21 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile',
            new_name='profile_picture',
        ),
    ]