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
    


    
    # path('create_account_success/' , views.ExecCreateAccount.as_view(), name= 'create_done'),
    # path('create_account_success' , views.CreateAccountView.create_done, name= 'create_done'),
    # path('create_account_success/<int:pk>/<str:user_id>' , views.CreateAccountView.create_done, name= 'create_done'),
    # path('create_account_success/<int:pk>', views.TableDetailView.as_view(), name='table'), # 追加
    # path('/login_success', views.login_success, name='login_success'),
    # path('login/<int:pk>/', views.login_success, name='login_success'),
]