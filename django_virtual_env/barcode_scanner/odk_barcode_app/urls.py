from django.urls import path
from . import views

urlpatterns = [
    path('odk_barcode_app/login', views.ona_connector, name='login'),
    path('odk_barcode_app/scanner', views.scanner, name='scanner'),
    path('odk_barcode_app/record', views.display_data, name='record'),
]