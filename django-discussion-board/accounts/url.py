from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name='accounts'

urlpatterns = [
path('signup/',views.signup,name="signup"),
path('logout/',auth_views.LogoutView.as_view(),name="logout"),
path('login/',auth_views.LoginView.as_view(template_name="login.html"),name="login"),
path('account/',views.UserUpdateView.as_view(),name='my_account'),
path('changepassword/',auth_views.PasswordChangeView.as_view(template_name="change_password.html"),name="change_password"),
path('changepassword/done/',auth_views.PasswordChangeDoneView.as_view(template_name="change_password_done.html"),name="change_passworddone"),
]
