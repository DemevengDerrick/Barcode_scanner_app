from django.http import HttpResponse
from django.template import loader

def scanner(request):
    template = loader.get_template('scanner.html')
    return HttpResponse("This is the scanner page")

def ona_connector(request):
    template = loader.get_template('login.html')
    return HttpResponse("This is the ONA Login page")

def display_data(request):
    template = loader.get_template('record.html')
    return HttpResponse("This is the data page")

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())