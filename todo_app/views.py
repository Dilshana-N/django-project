from django.shortcuts import render

# Create your views here.
def test(request):
    return render(request,"test.html")
def home(request):
    return render(request,"home.html")
def index(request):
    return render(request,"index.html")
def indexx(request):
    return render(request,"indexx.html")

