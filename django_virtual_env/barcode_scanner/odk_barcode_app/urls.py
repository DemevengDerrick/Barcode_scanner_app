from django.urls import path
from . import views

urlpatterns = [
    path('odk_barcode_app/', views.ona_connector, name='ona_connector'),
]