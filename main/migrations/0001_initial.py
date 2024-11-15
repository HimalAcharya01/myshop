# Generated by Django 5.1 on 2024-08-15 05:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='products')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='products')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='products')),
                ('name', models.CharField(max_length=30)),
                ('desc', models.TextField()),
                ('mark_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('dicscount_percentage', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price', models.DecimalField(decimal_places=2, editable=False, max_digits=10)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category')),
                ('Subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.subcategory')),
            ],
        ),
    ]
