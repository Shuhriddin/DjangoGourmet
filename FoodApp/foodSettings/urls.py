"""
URL configuration for foodSettings project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# static files
from django.conf import settings
from django.conf.urls.static import static
# users
from users import views as user_views
# users login and logout
from django.contrib.auth import views as autentificate_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('food/', include('app.urls')),
    path('', user_views.register, name='register'),
    path('login/', autentificate_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    # logout users: views.py da funksiya yangi
    path('logout/', user_views.custom_logout, name='logout'),
    path('profile/', user_views.profile, name='profile'),
]

urlpatterns += [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)