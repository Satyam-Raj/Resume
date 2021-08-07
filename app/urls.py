from django.urls import path
from . import views


urlpatterns = [
    path('home', views.home_view, name='home'),
    path('', views.index_view, name='index'),
    path('login', views.login_view, name='login'),
    path('register', views.register_view, name='register'),
    path('about', views.about_view, name='about'),
    path('contact', views.contact_view, name='contact'),
    path('subscription', views.subscription_view, name='subscription'),
    path('edit_profile', views.profile_update_view, name='edit_profile'),
    path('profile/<username>', views.profile_view, name='profile'),
    path('logout', views.logout_view, name='logout'),
    path('<str:pk>', views.try_view, name='try'),
]