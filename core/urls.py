from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('talking/', views.talking_view, name='lets_talk'),
    path('safaricom_report/', views.safaricom_report, name='safaricom_report'),
]
