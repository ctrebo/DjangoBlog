from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from .models import BlogComment, Blog, BlogAuthor

import datetime

# Create your views here.
def index(request):
    num_blogs = Blog.objects.all().count()

    context = {
        "num_blogs": num_blogs,
    }

    return render(request, 'index.html', context=context)


class BlogListView(generic.ListView):
    model = Blog

class BlogDetailView(generic.DetailView):
    model = Blog

class BlogAuthorListView(generic.ListView):
    model = BlogAuthor

class BlogListbyAuthorView(generic.ListView):
    """
    Generic class-based view for a list of blogs posted by a particular BlogAuthor.
    """
    model = Blog
    paginate_by = 5
    template_name ='blog/blog_list_by_author.html'
    
    def get_queryset(self):
        """
        Return list of Blog objects created by BlogAuthor (author id specified in URL)
        """
        id = self.kwargs['pk']
        target_author=get_object_or_404(BlogAuthor, pk = id)
        return Blog.objects.filter(author=target_author)
        
    def get_context_data(self, **kwargs):
        """
        Add BlogAuthor to context so they can be displayed in the template
        """
        # Call the base implementation first to get a context
        context = super(BlogListbyAuthorView, self).get_context_data(**kwargs)
        # Get the blogger object from the "pk" URL parameter and add it to the context
        context['blogger'] = get_object_or_404(BlogAuthor, pk = self.kwargs['pk'])
        context["height"] = "200px"
        context["width"] = "200px"
        return context


class BlogCommentCreate(LoginRequiredMixin, CreateView):
    model = BlogComment
    fields = ['description',]

    def get_context_data(self, **kwargs):
        """
        Add associated blog to form template so can display its title in HTML.
        """
        # Call the base implementation first to get a context
        context = super(BlogCommentCreate, self).get_context_data(**kwargs)
        context["blog"] = get_object_or_404(Blog, pk = self.kwargs['pk']) 
        return context
        
    def form_valid(self, form):
        """
        Add author and associated blog to form data before setting it as valid (so it is saved to model)
        """
        #Add logged-in user as author of comment
        form.instance.author = self.request.user
        #Associate comment with blog based on passed id
        form.instance.blog=get_object_or_404(Blog, pk = self.kwargs['pk'])
        # Call super-class form validation behaviour
        return super(BlogCommentCreate, self).form_valid(form)

    def get_success_url(self):
        """
        After posting comment return to blog page
        """
        return reverse("blog-detail", kwargs={'pk': self.kwargs['pk'],})

class BlogCommentDelete(LoginRequiredMixin, DeleteView):
    model = BlogComment

    def get_success_url(self):
        return reverse("blog-detail", kwargs={'pk': self.kwargs['pk'],})
class BlogUpdate(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = ['name', 'description']

    success_url = reverse_lazy("blogs")


class BlogDelete(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy("blogs")

class BlogAuthorUpdate(LoginRequiredMixin, UpdateView):
    model = BlogAuthor
    fields = ['bio', 'prof_picture']

    success_url = reverse_lazy("profpage-user")


class ProfilPageListView(LoginRequiredMixin, generic.ListView):
    model = Blog
    template_name = "blog/profil_page_by_user.html"

    def get_queryset(self):
        blog_author = BlogAuthor.objects.get(user = self.request.user)
        return Blog.objects.filter(author=blog_author)

    def get_context_data(self):
        """
        add data of user that is loged in to context variable
        """
        context = super(ProfilPageListView, self).get_context_data()
        context["blogger"] = BlogAuthor.objects.get(user=self.request.user)
        # authors = BlogAuthor.objects.get(user=self.request.user)
        context["num_blogs_user"] = Blog.objects.filter(author__user=self.request.user).count()
        return context

class SeeNewBlogsListView(LoginRequiredMixin, generic.ListView):
    model = Blog
    template_name = "blog/see_new_blog.html"

    def get_queryset(self):
        return Blog.objects.all().exclude(author__user=self.request.user).filter(post_date__gte = datetime.date.today() - datetime.timedelta(hours=24))


