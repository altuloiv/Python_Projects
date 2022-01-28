# Generated by Django 4.0.1 on 2022-01-28 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='djangoClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=60)),
                ('CourseNumber', models.IntegerField(default='')),
                ('InstructorName', models.CharField(default='', max_length=60)),
                ('Duration', models.FloatField()),
            ],
        ),
    ]