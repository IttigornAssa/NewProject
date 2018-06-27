from django.urls import path,include
from django.contrib import admin
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('form/', views.model_form_upload, name='form'),
    path('oauth/', include('social_django.urls', namespace='social')),  
    path('admin/', admin.site.urls),
    path('', views.listPerson, name='home'),
    path('home/', views.home, name='home1'),
    path(r'logout/', auth_views.logout, {'next_page'}, name='logout'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

