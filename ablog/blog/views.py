from typing import Any
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import post, category, comment
from .forms import postform, Editform, Commentform
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# # Create your views here.
def Likeview(request, pk):
     posts =  get_object_or_404(post, id=request.POST.get('post_id'))
     liked = False
     if posts.likes.filter(id=request.user.id).exists():
          posts.likes.remove(request.user)
          liked = False
     else:
          posts.likes.add(request.user)
          liked = True
     return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))

     
     
class Homeview(ListView):
     model = post
     template_name = 'blog/home.html'
     cats = category.objects.all()
     ordering = ['-post_date']
     
     def get_context_data(self, *args, **kwargs):
          cat_menu = category.objects.all()
          context = super(Homeview, self).get_context_data(*args, **kwargs)
          context["cat_menu"] = cat_menu
          return context
     
   
def CategoryListview(request):
     cat_menu_list = category.objects.all()
     return render(request, 'category_list.html', {'cat_menu_list':cat_menu_list})     
     
def Categoryview(request, cats):
     category_posts = post.objects.filter(category=cats.replace('-', ' '))
     return render(request, 'categories.html', {'cats':cats.title().replace('-', ' '), 'category_posts':category_posts,})
    
class ArticleDetailview(DetailView):
    model = post
    template_name = 'blog/article_details.html'
    
    def get_context_data(self, *args, **kwargs):
         cat_menu = category.objects.all()
         context = super(ArticleDetailview, self).get_context_data(*args, **kwargs)
         
         stuff = get_object_or_404(post, id=self.kwargs['pk'])
         total_likes = stuff.total_likes()
         
         liked = False
         if stuff.likes.filter(id=self.request.user.id).exists():
              liked = True
         
         context["cat_menu"] = cat_menu
         context["total_likes"] = total_likes
         context["liked"] = liked
         return context
    
class Addpostview(CreateView):
     model = post
     form_class = postform
     template_name = 'add_post.html'
     # fields = '__all__'
     
class Addcommentview(CreateView):
     model = comment
     form_class = Commentform
     template_name = 'add_comment.html'
     
     def form_valid(self, form):
          form.instance.post_id = self.kwargs['pk']
          return super().form_valid(form)
     # fields = '__all__'
     success_url = reverse_lazy('home')
     
class Addcategoryview(CreateView):
     model = category
     # form_class = postform
     template_name = 'add_category.html'
     fields = '__all__'

class Updatepostview(UpdateView):
     model = post
     form_class = Editform        
     template_name = 'update_post.html'
     # fields = ['title', 'title_tag', 'body']
     
class Deletepostview(DeleteView):
     model = post
     template_name = 'delete_post.html'
     success_url = reverse_lazy('home')
     
def login_user(request):
     if request.method == "POST":
          username = request.POST['username']
          password = request.POST['password']
          user = authenticate(request, username = username, password = password)
          
          if user is not None:
               login(request, user)
               messages.success(request, ("Hi there"))
               return redirect('home')
          
          else:
               messages.success(request, ("Your password is incorrect"))
               return redirect('login')
          
     else:
          return render(request, 'blog/login.html', {})
     
def logout_user(request):
     logout(request)
     messages.success(request, ("You've logged out!"))
     return redirect('login')