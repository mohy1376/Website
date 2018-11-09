# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render



from django.shortcuts import render,redirect

from django.contrib.auth import authenticate,login

from django.views.generic import View

from django.views.generic.edit import CreateView,UpdateView,DeleteView

from django.http import HttpResponse



from django.contrib.auth import logout

from .models import comment
# Create your views here.
class about(View):
    template_name = 'comment/about.html'

    def get(self,request):
        return render (request,self.template_name)

    def post(self,request):
        text =  request.POST.get("comments")
        name =  request.POST.get("name")
        email = request.POST.get("email")
        newComment = comment(text=text,name=name,email=email)
        newComment.save()
        return redirect('/')
