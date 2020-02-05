from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from DjangoUeditor.models import UEditorField
# from orgs.models import Publisher, Author

User = get_user_model()


class YgCategory(models.Model):
    catname = models.CharField(max_length=25, verbose_name='员工类别')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    def __str__(self):
        return self.catname

    class Meta:
        verbose_name = '类别'
        verbose_name_plural = verbose_name


class YgTag(models.Model):
    tagname = models.CharField(max_length=25, verbose_name='标签名称')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    def __str__(self):
        return self.tagname

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name


class Bm(models.Model):
    name = models.CharField(max_length=25, verbose_name='部门')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '部门'
        verbose_name_plural = verbose_name




class Yg(models.Model):
    category = models.ForeignKey(YgCategory, verbose_name="人员类别", null=True, blank=False, on_delete=models.SET_NULL)
    bm = models.ForeignKey(Bm, verbose_name="部门", null=True, blank=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(YgTag, blank=False, verbose_name="标签")
    name = models.CharField(max_length=255, verbose_name='姓名')
    sfz = models.CharField(max_length=18, verbose_name=u"身份证",default='612322', null=True, blank=True)
    sfz_img = models.ImageField(upload_to='yg', verbose_name='身份证图片', max_length=255, null=True,
                                blank=True)
    gender = models.CharField(verbose_name="性别", choices=(
        ("0", "男"), ("1", "女")),default='0', max_length=1)
    address = models.CharField(max_length=100, verbose_name=u"地址", default=u"")
    desc = UEditorField(verbose_name='简历', width=800, height=500, toolbars="full",
                        imagePath="yg/desc/", filePath="yg/desc/", blank=True, default="")

    mobile = models.CharField(max_length=11, verbose_name=u"手机", null=True, blank=True)
    is_zg = models.BooleanField(default='true', verbose_name=u"是否在岗")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '姓名'
        verbose_name_plural = verbose_name
        ordering = ('-updated_at',)

