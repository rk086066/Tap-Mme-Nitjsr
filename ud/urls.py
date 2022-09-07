from django.urls import path
from ud import views
urlpatterns = [
    path('', views.index, name='home'),

    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('pyqs', views.Pyqs, name='pyqs'),
    path('about', views.about, name='about'),
    path('resume', views.Resume, name='resume'),
    path('notice', views.Notice, name='notice'),
    path('contact', views.Contact, name='contact'),
    path('contactlist', views.ContactedList, name='contactlist'),
    path('resumelist', views.ResumeList, name='resumelist'),
]
