from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    chinese_name = models.CharField(max_length=128,default='',verbose_name="姓名")
    #image = models.ImageField(upload_to='photos/%Y/%m/%d/',default='',verbose_name="头像")
    age = models.PositiveIntegerField(verbose_name="年龄")
    occupation = models.CharField(max_length=100,null=True,blank=True,default='',verbose_name="职业")
    school = models.CharField(max_length=100,null=True,blank=True,default='',verbose_name="学校")
    country = models.CharField(max_length=100,null=True,blank=True,default='',verbose_name="国家")
    hometown = models.CharField(max_length=100,null=True,blank=True,default='',verbose_name="家乡")
    email = models.EmailField(default='',verbose_name="电子邮箱")
    phone = models.CharField(max_length=100, null=True, blank=True, default='',verbose_name="电话")
    qq = models.CharField(max_length=100, null=True, blank=True, default='',verbose_name="qq")
    wechat = models.CharField(max_length=100, null=True, blank=True, default='',verbose_name="微信")
    homepage = models.URLField(verbose_name="个人主页")
    content = models.TextField(verbose_name="自我介绍",default='')
    class Meta:
        verbose_name = verbose_name_plural = "用户信息"

class skills(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0 
    STATUS_ITEMS = (
        (STATUS_NORMAL,'正常'),
        (STATUS_DELETE,'删除'),
    )
    ICON_NORMAL = 1
    ICON_WITHOUT = 0 
    CHOICE_ITEMS = (
        (ICON_NORMAL,'有图标'),
        (ICON_WITHOUT,'无图标'),
    ) 
    ICON_ITEMS = (
        ("icon-screen-smartphone",'icon-screen-smartphone'),
        ("icon-basic-keyboard",'icon-basic-keyboard'),
        ("icon-basic-mouse",'icon-basic-mouse'),
    )
    skill = models.CharField(max_length=200,verbose_name="技能名称")
    status = models.PositiveIntegerField(default=STATUS_NORMAL,choices=STATUS_ITEMS,verbose_name="状态")
    with_icon = models.PositiveIntegerField(default=ICON_NORMAL,choices=CHOICE_ITEMS,verbose_name="有无图标") 
    icon = models.CharField(max_length=200,default=ICON_ITEMS[0][0],null=True, blank=True,choices=ICON_ITEMS,verbose_name="图标")
    length = models.PositiveIntegerField(null=True, blank=True,verbose_name="进度条长度") 
    content =models.TextField(verbose_name="技能介绍",default='')
    owner = models.ForeignKey(User,verbose_name="技能属主",on_delete=models.CASCADE)
    def __str__(self):
        return self.skill+self.owner.username
    class Meta:
        verbose_name = verbose_name_plural = "技能"

class eduction(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0 
    STATUS_ITEMS = (
        (STATUS_NORMAL,'正常'),
        (STATUS_DELETE,'删除'),
    )
    KIND_EDUCTION = 1
    KIND_EXPERIENCE = 0 
    STATUS_IEDUCTION = (
        (KIND_EDUCTION ,'教育经历'),
        (KIND_EXPERIENCE,'个人经历'),
    )
    name = models.CharField(max_length=100,verbose_name="经历名称")
    status = models.PositiveIntegerField(default=STATUS_NORMAL,choices=STATUS_ITEMS,verbose_name="状态")
    kind = models.PositiveIntegerField(default=KIND_EDUCTION,choices=STATUS_IEDUCTION,verbose_name="经历种类") 
    degree = models.CharField(max_length=100,verbose_name="学历名称")
    start_time = models.DateField(verbose_name="开始时间")
    end_time = models.DateField(verbose_name="结束时间")
    owner = models.ForeignKey(User,verbose_name="经历属主",on_delete=models.CASCADE)
    content = models.TextField(verbose_name="经历介绍",default='')
    created_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")

    def __str__(self):
        return self.name+self.owner.username
    class Meta:
        verbose_name = verbose_name_plural = "经历"

class photos(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0 
    STATUS_ITEMS = (
        (STATUS_NORMAL,'正常'),
        (STATUS_DELETE,'删除'),
    )
    name = models.CharField(max_length=100,verbose_name="照片名称")
    kind = models.CharField(max_length=100,verbose_name="照片种类") 
    status = models.PositiveIntegerField(default=STATUS_NORMAL,choices=STATUS_ITEMS,verbose_name="状态")
    image = models.ImageField(upload_to='photos/%Y/%m/%d/',default='',verbose_name="图片") 
    content = models.TextField(verbose_name="图片介绍",default='')
    owner = models.ForeignKey(User,verbose_name="图片属主",on_delete=models.CASCADE)

    def __str__(self):
        return self.name+self.owner.username
    class Meta:
        verbose_name = verbose_name_plural = "照片"