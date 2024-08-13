# Generated by Django 5.0.3 on 2024-08-13 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_name', models.CharField(blank=True, max_length=200, null=True)),
                ('blog_description', models.CharField(blank=True, max_length=200, null=True)),
                ('blog_image', models.ImageField(upload_to='blog_images/')),
            ],
        ),
    ]
