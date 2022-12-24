from django.urls import path

from .views import SignUpView

app_name = 'userbase'

urlpatterns = [
    path('',SignUpView.as_view(),name='signup')
]
