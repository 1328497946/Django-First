# Generated by Django 2.1.7 on 2019-12-26 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CHANGE',
            fields=[
                ('ID_CHA', models.IntegerField(default=0, primary_key=True, serialize=False, verbose_name='记录号')),
                ('REC_TIME', models.DateField(default='', verbose_name='记录时间')),
                ('DESCRIPTION', models.CharField(max_length=200, verbose_name='描述')),
            ],
            options={
                'verbose_name_plural': '学籍信息变更表',
                'db_table': 'CHANGE',
            },
        ),
        migrations.CreateModel(
            name='CHANGE_CODE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CODE', models.IntegerField(default=0, verbose_name='学籍变更代码')),
                ('DESCRIPTION', models.CharField(max_length=10, verbose_name='学籍变更说明')),
            ],
            options={
                'verbose_name_plural': '学籍变更代码表',
                'db_table': 'CHANGE_CODE',
            },
        ),
        migrations.CreateModel(
            name='CLASS',
            fields=[
                ('ID_CLA', models.IntegerField(default=1, primary_key=True, serialize=False, verbose_name='班级编号')),
                ('NAME_CLA', models.CharField(max_length=20, verbose_name='班级全称')),
            ],
            options={
                'verbose_name_plural': '班级信息表',
                'db_table': 'CLASS',
            },
        ),
        migrations.CreateModel(
            name='DEPARTMENT',
            fields=[
                ('ID_DEP', models.IntegerField(default=1, primary_key=True, serialize=False, verbose_name='院系编号')),
                ('NAME_DEP', models.CharField(max_length=20, verbose_name='全称')),
            ],
            options={
                'verbose_name_plural': '院系信息表',
                'db_table': 'DEPARTMENT',
            },
        ),
        migrations.CreateModel(
            name='PUNISH_CODE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CODE', models.IntegerField(default=0, verbose_name='处罚级别代码')),
                ('DESCRIPTION', models.CharField(max_length=20, verbose_name='处罚级别说明')),
            ],
            options={
                'verbose_name_plural': '处罚级别代码表',
                'db_table': 'PUNISH_CODE',
            },
        ),
        migrations.CreateModel(
            name='PUNISHMENT',
            fields=[
                ('ID_PUN', models.IntegerField(default=0, primary_key=True, serialize=False, verbose_name='记录号')),
                ('ENABLE', models.BooleanField(default=True, verbose_name='是否生效')),
                ('REC_TIME', models.DateField(default='', verbose_name='记录时间')),
                ('DESCRIPTION', models.CharField(max_length=200, verbose_name='描述')),
                ('LEVELS', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.PUNISH_CODE', verbose_name='级别代码')),
            ],
            options={
                'verbose_name_plural': '处罚记录信息表',
                'db_table': 'PUNISHMENT',
            },
        ),
        migrations.CreateModel(
            name='REWARD',
            fields=[
                ('ID_REW', models.IntegerField(default=0, primary_key=True, serialize=False, verbose_name='记录号')),
                ('REC_TIME', models.DateField(default='', verbose_name='记录时间')),
                ('DESCRIPTION', models.CharField(max_length=200, verbose_name='描述')),
            ],
            options={
                'verbose_name_plural': '奖励记录信息表',
                'db_table': 'REWARD',
            },
        ),
        migrations.CreateModel(
            name='REWARD_CODE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CODE', models.IntegerField(default=0, verbose_name='奖励级别代码')),
                ('DESCRIPTION', models.CharField(max_length=20, verbose_name='奖励级别说明')),
            ],
            options={
                'verbose_name_plural': '奖励级别代码表',
                'db_table': 'REWARD_CODE',
            },
        ),
        migrations.CreateModel(
            name='STUDENT',
            fields=[
                ('STUDENTID', models.IntegerField(default=1, primary_key=True, serialize=False, verbose_name='学号')),
                ('NAME_STU', models.CharField(max_length=20, verbose_name='姓名')),
                ('SEX', models.CharField(choices=[('男', '男'), ('女', '女')], max_length=5, verbose_name='性别')),
                ('BIRTHDAY', models.DateField(verbose_name='生日')),
                ('NATIVE_PLACE', models.CharField(max_length=50, verbose_name='籍贯')),
                ('ID_CLA', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.CLASS', verbose_name='班级')),
                ('ID_DEP', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.DEPARTMENT', verbose_name='所属院系')),
            ],
            options={
                'verbose_name_plural': '学生个人信息表',
                'db_table': 'STUDENT',
            },
        ),
        migrations.AddField(
            model_name='reward',
            name='LEVELS',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.REWARD_CODE', verbose_name='级别代码'),
        ),
        migrations.AddField(
            model_name='reward',
            name='STUDENTID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.STUDENT', verbose_name='学号'),
        ),
        migrations.AddField(
            model_name='punishment',
            name='STUDENTID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.STUDENT', verbose_name='学号'),
        ),
        migrations.AddField(
            model_name='class',
            name='NAME_DEP',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.DEPARTMENT', verbose_name='所属院系'),
        ),
        migrations.AddField(
            model_name='change',
            name='CHANGE',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.CHANGE_CODE', verbose_name='变更代码'),
        ),
        migrations.AddField(
            model_name='change',
            name='STUDENTID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.STUDENT', verbose_name='学号'),
        ),
    ]
