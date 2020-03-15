# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse

from .models import Todo
from .forms import Form_View

# Create your views here.
def todo_view(request):
    todos = Todo.objects.all()
   

    context = {
        'todos' : todos
    }
    
    return render(request, 'home.html', context)


def about_view(request, id):
    todo_id = Todo.objects.get(id=id)
    #forms  = Form_View(request.POST)

    context ={
        'todo_id': todo_id
        #'forms' : forms
    }
    
    return render(request, "about.html", context)

def update(request):
    if request.method == 'POST':
        name = request.POST.get('name', False)
        texts = request.POST.get('texts', False)

        todoo = Todo(name=name, texts=texts)
        todoo.save()
        return redirect('Home')

    else:
      
        return render(request, 'forms.html')


def deleteTodo(request, id):
    Todo.objects.filter(id=id).delete()

    return redirect(reverse("Home"))