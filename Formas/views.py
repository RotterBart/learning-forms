from django.shortcuts import render
from .forms import Userform, comments #импортируем класс который создали
from django.http import HttpResponse


#функция для отправки данных на сервер и вывод на экран
def index(request):
    if request.method == "POST":
        name = request.POST.get("name") #обращаемся к форме которая описана в классе Userform
        age = request.POST.get("age") #здесь тоже
        return HttpResponse(f"<h1>Привет, {name}, твой возраст: {age}</h1>")#выводим цю хуйню
    else:
        userform = Userform() #это сделано для того чтобы форма отображалась
        commentform = comments()
        return render(request, "index.html", {"form": userform, "comms": commentform }) 
