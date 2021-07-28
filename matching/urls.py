from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.TopView.topDispView, name = 'top'),
    path('login/' , views.LoginView.as_view() ,name = 'login'),
    path('logout/' , views.LogoutView.logout ,name = 'logout'),
    path('login_success/' , views.LoginSuccessView.login),
    path('create_account/' , views.CreateAccountView.as_view(), name= 'create'),
    path('create_account_success/' , views.CreateAccountView.as_view(), name= 'create_done'),
    path('chat/' , views.ChatView.as_view() ,name = 'chat'),
    path('profile/' , views.ProfileView.profile ,name = 'profile'),
    path('user_list/' , views.UserListView.display_list_view ,name = 'user_list'),
    path('ajax-number/' , views.UserListView.ajax_number ,name = 'ajax_number'),
    path('like_list/',views.LikeListView.display_Like_list_view ,name = 'like_list'),
    path('ajax-number/' , views.LikeListView.ajax_number ,name = 'ajax_number'),
    ] 