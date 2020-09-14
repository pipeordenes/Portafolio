from django.shortcuts import render, get_object_or_404

def index(request):
    return render(request, 'index.html', context={},)

def login(request):
    return render(request, 'login.html', {})