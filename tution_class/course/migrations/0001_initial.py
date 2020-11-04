# Generated by Django 3.1.3 on 2020-11-04 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=30)),
                ('duration', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('fees', models.IntegerField()),
            ],
        ),
    ]