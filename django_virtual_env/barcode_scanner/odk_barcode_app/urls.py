from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('odk_barcode_app/', views.scanner, name='scanner'),
    path('odk_barcode_app/login', views.ona_connector, name='ona_connector'),
    path('odk_barcode_app/record', views.display_data, name='record'),
]