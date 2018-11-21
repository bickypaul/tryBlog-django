from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import BlogPost
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

# all the post list view
class PostListView(ListView):
    model = BlogPost
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3

# specific user's post list view
class UserPostListView(ListView):
    model = BlogPost
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return BlogPost.objects.filter(author=user).order_by('-date_posted')

# post detail view
class PostDetailView(DetailView):
    model = BlogPost


# Post Create View
class PostCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost
    fields = ['title', 'content', 'blog_image']
    #template_name = blogpost_form.html

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
# Post Update View    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BlogPost
    fields = ['title', 'content', 'blog_image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# Post Delete View
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BlogPost
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
# the about page    
def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
