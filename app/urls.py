from django.urls import path
from django.contrib.auth import views as auth_views
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
    path('profile', views.profile_view, name='profile'),
    path('logout', views.logout_view, name='logout'),
    path('search', views.search_view, name='search'),
    path('profile_search/<int:pk>', views.Profile_search_view.as_view(), name='profile_search'),

    
    # down you can find the url for reset password    

    path('reset_password', auth_views.PasswordResetView.as_view(template_name='forgot_password/password_reset.html'), name='reset_password'),
    path('reset_password_sent',auth_views.PasswordResetDoneView.as_view(template_name='forgot_password/password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='forgot_password/password_reset_form.html' ), name='password_reset_confirm'),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name='forgot_password/password_reset_done.html'), name='password_reset_complete'),
    



]