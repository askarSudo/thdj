from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('', include('blog.urls')),
    path('опыт/', include('works.urls')),
    path('музыка/', include('audio.urls')),
    path('программы/', include('prog.urls')),
    path('учебники/', include('book.urls')),
    path('admin/', admin.site.urls),
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
