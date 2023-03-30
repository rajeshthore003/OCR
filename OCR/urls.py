
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from minor import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path( '',include('minor.urls')),
    path('predicttext', views.predicttext, name ='predicttext'),
    
    
]

# we just adding the New URLS files
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)