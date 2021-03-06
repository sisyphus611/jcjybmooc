# Generated by Django 2.1.4 on 2019-05-14 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='address',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='birthday',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='nick_name',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='class_name',
            field=models.CharField(default='', max_length=200, verbose_name='专业班级'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='department_name',
            field=models.CharField(choices=[('ysjyx', '艺术教育系'), ('yssjx', '艺术设计系'), ('whglx', '文化管理系'), ('yxbyx', '艺术表演系')], default='ysjyx', max_length=50, verbose_name='所属系部'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='real_name',
            field=models.CharField(default='请输入真实的姓名', max_length=50, verbose_name='真实的姓名'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='school_name',
            field=models.CharField(choices=[('cy', '重庆文化艺术职业学院'), ('outside_school', '其他学校')], default='cy', max_length=200, verbose_name='所属学校'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='student_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='学号'),
        ),
    ]
