from django.shortcuts import render




def index(request):
    
    return render(request, 'error/index.html')


def error_404(request, exception):
    return render(request, 'error/error404.html')
