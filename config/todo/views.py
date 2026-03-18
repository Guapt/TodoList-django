from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def todo_list(request, id=None):
    todo_lists = Todo.objects.all()
    return render(request, 'list.html', {'todo_lists': todo_lists})

def todo_add(request, id = None):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status')

        if not title or not description or not status:
            if not title:
                return render(request, 'add.html', {'error': 'title not found.'})
            elif not description:
                return render(request, 'add.html', {'error': 'description not found.'})
            else:
                return render(request, 'add.html', {'error': 'status not found.'})

        Todo.objects.create(title= title, description = description, status = status)
        return redirect('todo_list')

    return render(request, 'add.html')

def todo_edit(request, id = None):
    todo = Todo.objects.get(id = id)
    
    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        todo.status = request.POST.get('status')

        todo.save()
        return redirect('todo_list')

    return render(request, 'edit.html', {'todo':todo})

def todo_delete(request, id = None):
    todo = Todo.objects.get(id = id)

    if todo:
        todo.delete()
        return redirect('todo_list')

def completed(request):
    todo_lists = Todo.objects.filter(status='fullfilled')
    print('hi', todo_list)
    return render(request, 'list.html', {'todo_lists': todo_lists})

def pending(request):
    todo_lists = Todo.objects.filter(status__startswith ='p')
    return render(request, 'list.html', {'todo_lists': todo_lists})

def reject(request):
    todo_lists = Todo.objects.filter(status='rejected')
    return render(request, 'list.html', {'todo_lists': todo_lists})

def search(request):
    search= request.POST.get('search')
    todo_lists = Todo.objects.filter(title__icontains=search)
    return render(request, 'list.html', {'todo_lists': todo_lists, 'search' : search})








