from django.contrib import admin
from django.urls import path, include
from accounts import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register', views.register, name='register'),
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    # path('vehicle/', include('vehicle.urls')),
    path('agency/', include('agency.urls')),
    path('password-reset/',
        auth_views.PasswordResetView.as_view(
            template_name='registration/password_reset.html'
        ),
        name='password_reset'),
    path('password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='registration/password_reset_done.html'
        ),
        name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='registration/password_reset_confirm.html'
        ),
        name='password_reset_confirm'),
    path('password-reset-complete/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='registration/password_reset_complete.html'
        ),
        name='password_reset_complete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
