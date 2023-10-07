from django.shortcuts import render
import socket





def index(request):
    
    return render(request, 'error/index.html')


def error_404(request, exception):
    return render(request, 'error/error404.html')


def learn(request):
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    context = {'ip': ip}
    
    return render(request , 'error/learn.html'  , context)
