from travel import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'register',views.register,name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^profile/$', views.profile, name='profile'),
]