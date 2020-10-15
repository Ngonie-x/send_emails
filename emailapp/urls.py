from django.urls import path
from .views import email_form_view, index

app_name = 'emailapp'

urlpatterns = [
    path('send', email_form_view, name="email_form"),
    path('', index, name='home'),
]
