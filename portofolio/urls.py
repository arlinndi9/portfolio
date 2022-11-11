from django.urls import path, include
from portofolio import views
urlpatterns = [
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('project/',views.project,name='project'),
    path('contact/',views.contact,name='contact'),

]