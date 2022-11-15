from django.shortcuts import render
from .forms import Userform
from django.http import HttpResponse



def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        return HttpResponse(f"<h1>Привет, {name}, твой возраст: {age}</h1>")
    else:
        userform = Userform()
        return render(request, "index.html", {"form": userform })
