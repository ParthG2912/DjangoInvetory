from django.urls import include, path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('product/<int:id>/', views.product, name="product"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
]
