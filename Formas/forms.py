from django import forms







class Userform(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()