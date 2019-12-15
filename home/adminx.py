import xadmin
from .models import UserProfile,skills,eduction,photos,message

class BaseAdmin(object):
    def get_list_queryset(self):
        request = self.request
        qs = super().get_list_queryset()
        return qs

@xadmin.sites.register(UserProfile)
class UserProfileAdmin(BaseAdmin):
    list_display = ('chinese_name','age','occupation','school','country')

@xadmin.sites.register(skills)
class skillsAdmin(BaseAdmin):
    list_display = ('skill','status')


@xadmin.sites.register(eduction)
class eductionAdmin(BaseAdmin):
    list_display = ('name','kind','degree')

@xadmin.sites.register(photos)
class photosAdmin(BaseAdmin):
    list_display = ('name','kind')

@xadmin.sites.register(message)
class messageAdmin(BaseAdmin):
    list_display = ('name','subject')