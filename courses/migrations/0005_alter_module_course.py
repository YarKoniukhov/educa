# Generated by Django 4.1.6 on 2023-02-11 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_rename_courses_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modules', to='courses.course'),
        ),
    ]
