from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'index.html')
def codepage(request):
    return render(request, 'code.html')
def finish(request):
    return render(request, 'submit.html')
def sign(request):
    return render(request, 'master.html')
def last(request):
    return render(request, 'activity.html')
