# Generated by Django 5.1 on 2024-08-30 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_review_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image1',
            new_name='image',
        ),
    ]
