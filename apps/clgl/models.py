from datetime import datetime

from django.db import models
from django.urls import reverse
from DjangoUeditor.models import UEditorField
# Create your models here.


class Jsy(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"姓名")
    bm = models.CharField(max_length=1, verbose_name=u"所属部门",choices=(("0",u"客运队"),("1",u"公交公司")),default=0)
    jsz = models.CharField(max_length=18, verbose_name=u"驾驶证")
    zgz = models.CharField(max_length=20, verbose_name=u"资格证", null=True, blank=True)
    image = models.ImageField(default='', upload_to="clgl/jsz/", verbose_name=u"驾驶证", max_length=100)
    gender = models.CharField(verbose_name=u"性别", max_length=1, choices=(("0", u"男"), ("1", u"女")),
                              default="0")
    detail = UEditorField(verbose_name=u"简历", width=600, height=300, imagePath="clgl/jsy/ueditor/",
                          filePath="clgl/jsy/ueditor/", default='')
    address = models.CharField(max_length=100, verbose_name=u"地址", default=u"")
    mobile = models.CharField(max_length=11, verbose_name=u"手机", null=True, blank=True)
    cj_time = models.DateTimeField(default=datetime.now,verbose_name=u"参加工作时间")
    work_years = models.IntegerField(default=0, verbose_name=u"工作年限", null=True, blank=True)
    is_zg = models.BooleanField(default='true', verbose_name=u"是否在岗")
    age = models.IntegerField(default=18, verbose_name=u"年龄", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = u"驾驶员管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Spy(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"姓名")
    bm = models.CharField(max_length=1,verbose_name=u"所属部门", choices=(("0", u"客运队"), ("1", u"公交公司")),default=0)
    sfz = models.CharField(max_length=18, verbose_name=u"身份证")
    sgz = models.CharField(max_length=10, verbose_name=u"上岗证", null=True, blank=True)
    image = models.ImageField(default='', upload_to="clgl/spy/", verbose_name=u"照片", max_length=100)
    gender = models.CharField(verbose_name=u"性别", max_length=1, choices=(("0", u"男"), ("1", u"女")),
                              default="1")
    detail = UEditorField(verbose_name=u"简历", width=600, height=300, imagePath="clgl/spy/ueditor/",
                          filePath="clgl/spy/ueditor/", default='')
    address = models.CharField(max_length=100, verbose_name=u"地址", default=u"")
    mobile = models.CharField(max_length=11, verbose_name=u"手机", null=True, blank=True)
    cj_time = models.DateTimeField(default=datetime.now,verbose_name=u"参加工作时间")
    work_years = models.IntegerField(default=0, verbose_name=u"工作年限", null=True, blank=True)
    is_zg = models.BooleanField(default='true', verbose_name=u"是否在岗")
    age = models.IntegerField(default=18, verbose_name=u"年龄", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = u"售票员管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Bus_user(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"姓名")
    bm = models.CharField(max_length=1, verbose_name=u"所属部门",choices=(("0",u"客运队"),("1",u"公交公司")),default=0)
    sfz = models.CharField(max_length=18, verbose_name=u"身份证", null=True, blank=True)
    pic = models.ImageField(default='', upload_to="clgl/user/sfz/", verbose_name=u"照片", max_length=100)
    gender = models.CharField(verbose_name=u"性别", max_length=1, choices=(("0", u"男"), ("1", u"女")),
                              default="0")
    detail = UEditorField(verbose_name=u"简历", width=600, height=300, imagePath="clgl/user/ueditor/",
                          filePath="clgl/user/ueditor/", default='')
    address = models.CharField(max_length=100, verbose_name=u"地址", default=u"")
    mobile = models.CharField(max_length=11, verbose_name=u"手机", null=True, blank=True)
    cb_time = models.DateTimeField(default=datetime.now,verbose_name=u"经营时间")
    fujian = models.FileField(default='', upload_to="clgl/user/fj/", verbose_name=u"承包附件", max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = u"经营人管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Bus(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"车号",default=u'陕-')
    image = models.ImageField(default='', upload_to="clgl/bus", verbose_name=u"图片",max_length=100)
    desc = UEditorField(verbose_name=u"车辆简历", width=900, height=300, imagePath="clgl/cl/ueditor/", filePath="clgl/cl/ueditor/", default='')
    xsz = models.CharField(max_length=20, verbose_name=u"行驶证 ")
    yyz = models.CharField(max_length=20, verbose_name=u"营运证 ")
    rh_time = models.DateTimeField(default=datetime.now, verbose_name=u"入户时间")
    lxdj = models.CharField(max_length=1,verbose_name=u"类型等级",choices=(("0",u"中型中级"),("1",u"小型中级"),("2",u"高一级")))
    is_sy = models.BooleanField(default='true',verbose_name=u"是否审验")
    jsy = models.ForeignKey(Jsy,on_delete=models.SET_NULL, verbose_name=u"驾驶员", null=True, blank=True)
    spy = models.ForeignKey(Spy,on_delete=models.SET_NULL, verbose_name=u"售票员", null=True, blank=True)
    bm = models.CharField(verbose_name=u"管理部门", max_length=1, choices=(("0", u"客运队"), ("1", u"公交公司")),
                              default="0")
    bus_user = models.OneToOneField(Bus_user, blank=True, null=True, on_delete=models.SET_NULL,verbose_name=u"经营人")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')


    class Meta:
        verbose_name = u"车辆"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


