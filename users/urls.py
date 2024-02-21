from django.urls import path
from .views import signup_view, logout_confirm
from django.contrib.auth.views import  LogoutView, LoginView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView

urlpatterns=[
    path('signup/', signup_view, name="user-signup"),
    path("login/", LoginView.as_view(template_name='accounts/login.html'), name="user-login"),
    path("logout-confirm/", logout_confirm, name='logout-confirm'),
    path("logout/",LogoutView.as_view(template_name='accounts/logout.html'),name="user-logout"),
    path("reset-password/", PasswordResetView.as_view(template_name='accounts/password_reset.html'),name="reset-password"),
    path("password-reset-done/", PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path("password/<uidb64>/<token>/", PasswordResetConfirmView.as_view(template_name='accounts/reset.html'), name="password_reset_confirm"),
    path("password/complete/", PasswordResetCompleteView.as_view(template_name="accounts/complete.html"), name="password_reset_complete")
]