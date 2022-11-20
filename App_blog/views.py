from django.shortcuts import render,HttpResponseRedirect
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView,View,TemplateView
from App_blog.models import Blog,Comment,Likes
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from App_blog.forms import CommentForm
import uuid
# Create your views here.



class CreateBlog(LoginRequiredMixin,CreateView):
    model = Blog
    template_name = 'App_blog/create_blog.html'
    fields = ('blog_title','blog_content','blog_image')

    def form_valid(self, form):
        blog_obj = form.save(commit=False)
        blog_obj.author = self.request.user
        title = blog_obj.blog_title
        blog_obj.slug = title.replace(" ","-") +"-"+str(uuid.uuid4())
        blog_obj.save()
        return HttpResponseRedirect(reverse('index'))


class BlogList(ListView):
    context_object_name = 'blogs'
    model = Blog
    template_name = 'App_blog/blog_list.html'
    queryset = Blog.objects.order_by('-publishe_date')

@login_required
def blog_detail(request,slug):
    blog = Blog.objects.get(slug=slug)
    commentform = CommentForm()
    if request.method == 'POST':
        commentform = CommentForm(request.POST)
        if commentform.is_valid():
            comment = commentform.save(commit=False)
            comment.user = request.user
            comment.blog = blog
            comment.save()
            return HttpResponseRedirect(reverse('App_blog:blog_detail',kwargs={'slug':slug}))
    return render(request, 'App_blog/blog_detail.html',context={'blog':blog,'form':commentform})

