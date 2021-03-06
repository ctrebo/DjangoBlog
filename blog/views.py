from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.http import Http404


from .models import BlogComment, Blog, BlogAuthor
import datetime
#libraries for signup
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm





# Create your views here.

#signup view
def signup(request):
    """
    view that signes user up and creates a BlogAuthor object for the user
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            #add BlogAuthor of user
            new_blogauthor = BlogAuthor(user=user)
            new_blogauthor.save()
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def index(request):
    num_blogs = Blog.objects.all().count()

    context = {
        "num_blogs": num_blogs,
    }

    return render(request, 'index.html', context=context)


class BlogListView(LoginRequiredMixin, generic.ListView):
    """
    generic class-based view for a list of blogs
    """
    model = Blog

class BlogDetailView(LoginRequiredMixin, generic.DetailView):
    """
    Generic class-based view for a detailed description of a blog
    """
    model = Blog

class BlogAuthorListView(LoginRequiredMixin, generic.ListView):
    model = BlogAuthor

class BlogListbyAuthorView(LoginRequiredMixin, generic.ListView):
    """
    Generic class-based view for a list of blogs posted by a particular BlogAuthor.
    """
    model = Blog
    template_name ='blog/blog_list_by_author.html'
    
    def get_queryset(self):
        """
        Return list of Blog objects created by BlogAuthor (author id specified in URL)
        """
        try:
            id = self.kwargs['pk']
            target_author=get_object_or_404(BlogAuthor, pk = id)
            return Blog.objects.filter(author=target_author)
        except MyModel.DoesNotExist:
            raise Http404("No MyModel matches the given query.")

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
    """
    Generic edit view used to Create comments
    """
    model = BlogComment
    fields = ['description',]

    def get_context_data(self, **kwargs):
        """
        Add associated blog to form template so can display its title in HTML.
        """
        # Call the base implementation first to get a context
        context = super(BlogCommentCreate, self).get_context_data(**kwargs)
        context["blog"] = get_object_or_404(Blog, pk=self.kwargs['pk']) 
        return context
        
    def form_valid(self, form):
        """
        Add author and associated blog to form data before setting it as valid (so it is saved to model)
        """
        #Add logged-in user as author of comment
        form.instance.author = self.request.user
        #Associate comment with blog based on passed id
        form.instance.blog = get_object_or_404(Blog, pk=self.kwargs['pk'])
        # Call super-class form validation behaviour
        return super(BlogCommentCreate, self).form_valid(form)

    def get_success_url(self):
        """
        After posting comment return to blog page
        """
        return reverse("blog-detail", kwargs={'pk': self.kwargs['pk'],})

class BlogCreate(LoginRequiredMixin, CreateView):
    """
    Generic edit class-based view to create Blogs
    """
    model = Blog
    fields = ["name", "description"]
    success_url = reverse_lazy('blogs')

    def form_valid(self, form):
        #take logged-in user as BlogAuthor and add it as Blogauthor to blog
        blog_author = BlogAuthor.objects.get(user=self.request.user)
        form.instance.author = blog_author
        # Call super-class form validation behaviour
        return super(BlogCreate, self).form_valid(form)
    

class BlogCommentDelete(LoginRequiredMixin, DeleteView):
    """
    Generic edit view used to delete comments
    """
    model = BlogComment

    def get_success_url(self):
        """
        When deleting the comments is successful return the user to url written below
        """
        return reverse("blog-detail", kwargs={'pk': self.kwargs['pk'],})

class BlogUpdate(LoginRequiredMixin, UpdateView):
    """
    Generic edit view used to update blogs
    """
    model = Blog
    fields = ['name', 'description']

    success_url = reverse_lazy("blogs")


class BlogDelete(LoginRequiredMixin, DeleteView):
    """
    Generic edit view used to delete blogs
    """
    model = Blog
    success_url = reverse_lazy("blogs")

class BlogAuthorUpdate(LoginRequiredMixin, UpdateView):
    """
    Generic edit view used to update BlogAuthors
    """
    model = BlogAuthor
    fields = ['bio', 'prof_picture']

    success_url = reverse_lazy("profpage-user")


class ProfilPageListView(LoginRequiredMixin, generic.ListView):
    """
    generic class-based view for the users BlogAuthor data
    """

    model = Blog
    template_name = "blog/profil_page_by_user.html"

    def get_queryset(self):
        """
        get queryset of blogs that are written by the logged in user
        """
        try:
            blog_author = BlogAuthor.objects.get(user = self.request.user)
            return Blog.objects.filter(author=blog_author)
        except MyModel.DoesNotExist:
            raise Http404("No MyModel matches the given query.")

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
    """
    Generic edit class-based view for a list of Blogs written in a maximal time ago from the current time(logged in users blog excluded)
    """
    
    model = Blog
    template_name = "blog/see_new_blog.html"

    def get_queryset(self):
        """
        Add queryset of blogs written a maximum of 24h ago
        """
        try:
            return Blog.objects.all().exclude(author__user=self.request.user).filter(post_date__gte = datetime.date.today() - datetime.timedelta(hours=24))
        except MyModel.DoesNotExist:
            raise Http404("No MyModel matches the given query.")


