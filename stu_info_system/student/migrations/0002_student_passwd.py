# Generated by Django 2.1.7 on 2019-12-26 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='PASSWD',
            field=models.CharField(default='12345', max_length=20, verbose_name='密码'),
        ),
    ]
