from travel import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'register/$',views.register,name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'trip_planner/$', views.trip_planner, name='trip_planner'),
    url(r'trip_prev/', views.trip_prev, name='trip_prev'),
    url(r'user_input_result/', views.user_input_result, name='user_input_result'),
    url(r'save_user_services/', views.save_user_services, name='save_user_services'),
    url(r'success',views.success,name='success'),
    url(r'emergency/$', views.emergency, name='emergency'),
    url(r'homeVendor', views.homeVendor, name='homeVendor'),
    url(r'profileV', views.profileV, name='profileV'),
    url(r'emergencyV', views.emergencyV, name='emergencyV'),
    url(r'myPrevTripV', views.myPrevTripV, name='myPrevTripV'),
    url(r'contact/$', views.contact, name='contact'),
    url(r'contactV', views.contactV, name='contactV'),
    url(r'register_trip_vendor', views.registerTripVendor, name='registerTripVendor'),

]