from django.db import models
from datetime import datetime

from django.contrib.auth.models import AbstractUser


# Create your models here.


class UserProfile(AbstractUser):
    # 自定义的性别选择规则
    GENDER_CHOICES = (
        ("male", u"男"),
        ("female", u"女")
    )
    SCHOOL_CHOICES = (
        ("cy", u"重庆文化艺术职业学院"),
        ("outside_school", u"其他学校")
    )
    UNIVERSITE_DEPARTMENT_CHOICES = (
        ("ysjyx", u"艺术教育系"),
        ("yssjx", u"艺术设计系"),
        ("whglx", u"文化管理系"),
        ("yxbyx", u"艺术表演系")
    )
    # 真实姓名
    real_name = models.CharField(max_length=50, verbose_name=u"真实的姓名", default="请输入真实的姓名")
    # 所属学校
    school_name = models.CharField(
        max_length=200, 
        verbose_name=u"所属学校",
        choices=SCHOOL_CHOICES,
        default="cy"
    )
    # 所属系部
    department_name = models.CharField(
        max_length=50,
        verbose_name=u"所属系部",
        choices=UNIVERSITE_DEPARTMENT_CHOICES,
        default="ysjyx"
    )
    # 专业班级
    class_name = models.CharField(max_length=200, verbose_name=u"专业班级", default='')
    # 性别 只能男或女，默认女
    gender = models.CharField(
        max_length=6,
        verbose_name=u"性别",
        choices=GENDER_CHOICES,
        default="female")
    # 学号
    student_id = models.IntegerField(verbose_name=u"学号", null=True, blank=True)
    # 电话 
    mobile = models.CharField(
        max_length=11,
        null=True,
        blank=True,
        verbose_name=u"电话")
    # 头像 默认使用default.png
    image = models.ImageField(
        upload_to="image/%Y/%m",
        default=u"image/default.png",
        max_length=100,
        verbose_name=u"头像"
    )

    # meta信息，即后台栏目名
    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    # 重载__str__方法，打印实例会打印username，username为继承自AbstractUser
    def __str__(self):
        return self.username

    # 获取用户未读消息的数量
    def unread_nums(self):
        from operation.models import UserMessage
        return UserMessage.objects.filter(has_read=False, user=self.id).count()


class EmailVerifyRecord(models.Model):
    """邮箱验证码model"""
    SEND_CHOICES = (
        ("register", u"注册"),
        ("forget", u"找回密码"),
        ("update_email", u"修改邮箱"),
    )
    code = models.CharField(max_length=20, verbose_name=u"验证码")
    # 未设置null = true blank = true 默认不可为空
    email = models.EmailField(max_length=50, verbose_name=u"邮箱")
    send_type = models.CharField(
        choices=SEND_CHOICES,
        max_length=20,
        verbose_name=u"验证码类型")
    # 这里的now得去掉(),不去掉会根据编译时间。而不是根据实例化时间。
    send_time = models.DateTimeField(
        default=datetime.now, verbose_name=u"发送时间")

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name

    # 重载str方法使后台不再直接显示object

    def __str__(self):
        return '{0}({1})'.format(self.code, self.email)


class Banner(models.Model):
    """轮播图model"""
    title = models.CharField(max_length=100, verbose_name=u"标题")
    image = models.ImageField(
        upload_to="banner/%Y/%m",
        verbose_name=u"轮播图",
        max_length=100)
    url = models.URLField(max_length=200, verbose_name=u"访问地址")
    # 默认index很大靠后。想要靠前修改index值。
    index = models.IntegerField(default=100, verbose_name=u"顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name

    # 重载__str__方法使后台不再直接显示object

    def __str__(self):
        return '{0}(位于第{1}位)'.format(self.title, self.index)
