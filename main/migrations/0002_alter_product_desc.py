# Generated by Django 5.1 on 2024-08-16 04:40

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
