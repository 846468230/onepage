from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import UserProfile,message
# Create your views here.
from django.template import loader
def helloworld(request):
    return HttpResponse("Helloworld!")

def index(request,user_id=1):
    template = loader.get_template("home/index.html")
    user = UserProfile.objects.get(pk=user_id)
    context = {
            'user': user,
            "exp": user.exp(),
            "education": user.education(),
            "skills_with_icon": user.skills_with_icon(),
            "skills_without_icon": user.skills_without_icon(),
            "photos": user.photos(),
            "photos_kind":user.photos_kind(),
        }
    return HttpResponse(template.render(context,request))

class UserView(TemplateView):
    model = UserProfile
    template_name = 'home/index.html'
    def get(self,request,*args,**kwargs):
        user_id = self.kwargs.get('user_id')
        user = UserProfile.objects.get(pk=user_id)
        context = {
            'user': user,
            "exp": user.exp(),
            "education": user.education(),
            "skills_with_icon": user.skills_with_icon(),
            "skills_without_icon": user.skills_without_icon(),
            "photos": user.photos(),
            "photos_kind":user.photos_kind(),
        }
        return self.render_to_response(context)

'''def message_post(request,user_id = 1):
    messagea ={}
    user = UserProfile
    if request.POST:
        messagea['name'] = request.POST['name']
        messagea['email'] = request.POST['email']
        messagea['subject'] = request.POST['subject']
        messagea['message'] = request.POST['message']
        m = message

    return render(request, "post.html", ct'''