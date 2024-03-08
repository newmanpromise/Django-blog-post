from django.urls import path
from . import views
from .views import Homeview, ArticleDetailview, Addpostview, Updatepostview, Deletepostview, Addcategoryview, Categoryview, CategoryListview, Likeview, Addcommentview

urlpatterns = [
    path('', Homeview.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailview.as_view(), name='article-detail'),
    path('add_post', Addpostview.as_view(), name='add_post'),
    path('add_category', Addcategoryview.as_view(), name='add_category'),
    path('article/edit<int:pk>/', Updatepostview.as_view(), name='update_post'),
    path('article/<int:pk>/remove', Deletepostview.as_view(), name='delete_post'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('category/<str:cats>/', Categoryview, name='category'),
    path('category-list/',  CategoryListview, name='category-list'),
    path('like/<int:pk>', Likeview, name='like_post'),
    path('article/<int:pk>/comment/', Addcommentview.as_view(), name='add_comment'),
    
    
]