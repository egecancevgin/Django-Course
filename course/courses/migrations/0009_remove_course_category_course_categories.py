# Generated by Django 4.2 on 2023-04-26 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_alter_category_slug_alter_course_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='category',
        ),
        migrations.AddField(
            model_name='course',
            name='categories',
            field=models.ManyToManyField(to='courses.category'),
        ),
    ]
