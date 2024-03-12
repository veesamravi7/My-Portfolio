from django.urls import path
from myportfolio import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('resume/',views.resume,name='resume'),
    path('blog/',views.Blog,name='blog'),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)