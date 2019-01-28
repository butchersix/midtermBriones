from django.urls import path
from . import views

app_name= 'post'
urlpatterns = [
    path('', views.index, name='index'),
    path('help/', views.help, name='help'),
    path('<int:post_id>/', views.detail, name='details'),
    path('<int:post_id>/updatepost', views.update, name='updatepost'),
    path('createpost/', views.createPost, name='createpost'),
    path('<int:post_id>/createcomment/', views.createComment, name='createcomment')
]