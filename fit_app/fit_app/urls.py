from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from accounts.views import password_reset_request, login_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('login/', login_view, name='login'),
    path('accounts/', include('accounts.urls')),
    path('calculators/', include('calculators.urls')),
    path('hydration/', include('hydration.urls')),
    path('activities/', include('activities.urls')),
    path('sleep/', include('sleep.urls')),
    path('body_measurements/', include('body_measurments.urls')),
#    path('password_reset/', password_reset_request, name='password_reset'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
    path('password_reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm')

]

