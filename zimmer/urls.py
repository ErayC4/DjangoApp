from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static 
from tisch import views


urlpatterns = [
    path('', views.blog, name='blog'),
    path('create-post/', views.create_post, name='create-post'),
    path('<int:id>/', views.detail, name='detail'),
    #path('', include('django.contrib.auth.urls')),
    #path('sign-up', views.sign_up),
    path('post/edit/<int:post_id>/', views.edit_post, name='edit_post'),
    

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)