from django.shortcuts import render, redirect
from .models import Todo
# Create your views here.

def index(request):
    context = {}
    todos = Todo.get_all_todos()
    context['all_todos'] = todos
    if request.method == 'POST':
        title=request.POST['title']
        body=request.POST['body']
        Todo.objects.create(title = title, body = body)
        return redirect('home')
    return render(request, 'index.html', context)