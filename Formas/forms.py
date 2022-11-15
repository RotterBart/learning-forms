from django import forms


#класс содержащий формы для заполения имени и возраста, их можно юзать везде
class Userform(forms.Form):
    name = forms.CharField(label = "Имя", min_length=5)
    age = forms.IntegerField(label = "Возраст")

class comments(forms.Form):
    nickname = forms.CharField(label="Заголовок")
    vyser = forms.CharField(label="место для нахрюка", widget= forms.Textarea, help_text="хрюкните")