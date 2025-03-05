from django.urls import include, path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('product/<str:name>/', views.product, name="product"),
    path('user/<str:username>/', views.user, name="user"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
]
