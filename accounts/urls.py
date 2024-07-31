"""Definiuje wzorce adresów URL dla aplikacji accounts."""

from django.urls import path, include

from . import views

app_name = 'accounts'
urlpatterns = [
    # Dołączanie domyślnych adresów URL uwierzytelniania.
    path('', include('django.contrib.auth.urls')),
    # Strona rejestracji.
    path('register/', views.register, name='register'),
]