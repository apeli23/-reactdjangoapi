from django.shortcuts import render; #allows django to render a template file 

def index(request):
    return render(request, 'index.html')
