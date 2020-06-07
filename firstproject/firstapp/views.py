from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'firstapp/main.html')

def one(request):
    return render(request, 'firstapp/one.html')
    
def two(request):
    return render(request, 'firstapp/two.html')

def three(request):
    return render(request, 'firstapp/three.html')