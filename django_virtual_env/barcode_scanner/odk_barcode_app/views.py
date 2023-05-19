from django.shortcuts import render
from django.http import HttpResponse

def ona_connector(request):
    return HttpResponse("This will dispaly ONA data")