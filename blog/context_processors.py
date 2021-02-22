# context_processors.py
from .models import Blog, BlogComment, BlogAuthor

def profilepic_processor(request):
    navbar_profile_pic = ""
    if request.user.is_authenticated:
        navbar_profile_pic = BlogAuthor.objects.get(user=request.user)
    return {
        'navbar_profile_pic' : navbar_profile_pic
    }