from django.urls import path , include  
from . import views
from info import settings
from django.conf.urls.static import static
urlpatterns = [
    path('' , views.index , name = "index"), 
    path('articels/' , views.articles , name="articels"), 
    path('singleblog/<slug>/' , views.singleblog , name="singleblog") ,
    path('tinymce/', include('tinymce.urls')),

    
]+static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
