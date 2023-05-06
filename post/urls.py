
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:num>', views.index, name='index'),
    path('post/<int:pk>', views.post_detail, name='detail'),
    path('post/<int:pk>/delete', views.delete_post, name='delete'),
    path('post/create/', views.create_post, name='create'),
    path('post/<int:pk>/favorite', views.post_favorite, name='favorite'),
    path('post/explain', views.explain, name='explain'),
]