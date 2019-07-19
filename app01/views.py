# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse
import json
# Create your views here.

def index(request):
    # if request.method == "POST":
    #     i1=request.POST.get("i1")
    #     i2 = request.POST.get("i2")
    #     i3=int(i1)+int(i2)
    #     data={"i1":i1,"i2":i2,"i3":i3}
    #     return render(request,"index.html",{"i1":i1,"i2":i2,"i3":i3})
    return render(request,"index.html")

def calc(request):
    print(request.POST)
    i1 = request.POST.get("i1")
    i2 = request.POST.get("i2")
    i3 = int(i1) + int(i2)
    return HttpResponse(i3)

def calc1(request):
    print(request.POST)

    print(request.POST.get("i1"))
    print(json.loads(request.POST.get("info")))
    return HttpResponse("ok")


###https://www.cnblogs.com/maple-shaw/articles/9537309.html
from django import forms
from django.core.validators import RegexValidator
import re
from django.core.exceptions import ValidationError

def user_validate(value):
    user_re=re.compile(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
    if not user_re.match(value):
        raise ValidationError('someting is wrong')

class RegForm(forms.Form):
    user=forms.CharField(
        label="zhanghao",
        initial="lilyan",
        min_length=6,
        validators=[user_validate, ],
        # validators=[RegexValidator(r'^[0-9]+$',"please input number"),RegexValidator(r'^123[0-9]+$',"please input 123 number")],

        widget=forms.TextInput(attrs={"class":"form-control","placeholder":"User"}))
    pwd=forms.CharField(label="mima",widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password"}))
    gender=forms.fields.ChoiceField(
        choices=((1,"male"),(2,"femal"),(3,"secret")),
        label="xingbie",
        initial=2,
        widget=forms.widgets.Select()
    )
    hobby = forms.fields.MultipleChoiceField(
        choices=((1, "basketball"), (2, "football"), (3, "doubleball"),),
        label="aihao",
        initial=[1, 3],
        widget=forms.widgets.SelectMultiple()
    )


def aboutform(request):
    form_obj = RegForm()
    if request.method == "POST":
        print(request.POST)
        form_obj = RegForm(request.POST)
        if form_obj.is_valid():
            return HttpResponse("hello lily")
    return render(request,"aboutform.html",{"form_obj":form_obj})

######global gouzi
# def clean(self):
#     pwd=self.cleaned_data.get("pwd")
#     re_pwd=self.cleaned_data.get("pwd")
#     if pwd==re_pwd:
#         return self.cleaned_data
#     self.add_error("re_pwd","the pass is different twice")
#     raise ValidationError("the pass is different twice")

# ####scope gouzi function
# def clean_user(self):
#     value=self.cleaned_data.get("user")
#     if not re.match(r"^1[3-9]\d{9}$",value):
#         raise ValidationError("shou ji style is wrong")
#     return value