from django.db import models
from django.contrib.auth.models import User
from DjangoUeditor.models import UEditorField #头部增加这行代码导入UEditorField
# Create your models here.
# 文章



from django.db import models

class Treatment(models.Model):
    id =models.IntegerField(verbose_name='辩证论证id',primary_key=True,blank=True)
    range  = models.TextField('适用范围', max_length=300, blank=True)
    type = models.CharField('类型', max_length=70, blank=True)
    excerpt = models.TextField('临床表现', max_length=300, blank=True)
    bzimage = models.ImageField(upload_to='article_img', verbose_name='辩证的图片', blank=True, null=True)
    recommend = models.TextField('推荐处方', max_length=500, blank=True)
    prescription = models.TextField('基础方剂', max_length=300, blank=True)
    take = models.TextField('服用方法', max_length=3000, blank=True)
    medicine = models.TextField('推荐中成药', max_length=300, blank=True)
    acupoint = models.TextField('针灸穴位', max_length=300, blank=True)
    source = models.CharField('出处', max_length=70, blank=True)

    class Meta:
         verbose_name = '辨证论治'
         verbose_name_plural = verbose_name

    def __str__(self):
        return self.type
