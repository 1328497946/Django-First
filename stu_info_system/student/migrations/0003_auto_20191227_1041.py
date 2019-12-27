# Generated by Django 2.1.7 on 2019-12-27 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_student_passwd'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='change',
            options={'verbose_name': '学生', 'verbose_name_plural': '学籍信息变更表'},
        ),
        migrations.AlterModelOptions(
            name='change_code',
            options={'verbose_name': '变更代码', 'verbose_name_plural': '学籍变更代码表'},
        ),
        migrations.AlterModelOptions(
            name='class',
            options={'verbose_name': '班级', 'verbose_name_plural': '班级信息表'},
        ),
        migrations.AlterModelOptions(
            name='department',
            options={'verbose_name': '院系', 'verbose_name_plural': '院系信息表'},
        ),
        migrations.AlterModelOptions(
            name='punish_code',
            options={'verbose_name': '处罚代码', 'verbose_name_plural': '处罚级别代码表'},
        ),
        migrations.AlterModelOptions(
            name='punishment',
            options={'verbose_name': '学生', 'verbose_name_plural': '处罚记录信息表'},
        ),
        migrations.AlterModelOptions(
            name='reward',
            options={'verbose_name': '学生', 'verbose_name_plural': '奖励记录信息表'},
        ),
        migrations.AlterModelOptions(
            name='reward_code',
            options={'verbose_name': '奖项代码', 'verbose_name_plural': '奖励级别代码表'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': '学生', 'verbose_name_plural': '学生个人信息表'},
        ),
        migrations.AlterField(
            model_name='punish_code',
            name='CODE',
            field=models.IntegerField(verbose_name='处罚级别代码'),
        ),
    ]
