from django.shortcuts import render, redirect
from .models import ToDo
from django.utils.dateparse import parse_datetime

# Create your views here.
def task_list(request):
    tasks = ToDo.objects.all()
    return render(request, 'to_do.html', {'tasks': tasks})

def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        deadline_string = request.POST.get('deadline')
        if deadline_string:
            deadline = parse_datetime(deadline_string)
        else:
            deadline = None

        ToDo.objects.create(title=title, description=description, deadline=deadline)
        return redirect('task_list')

    return render(request, 'create_task.html')

def delete_task(request, task_id):
    task = ToDo.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')

def update_task(request, task_id):
    task = ToDo.objects.get(id=task_id)

    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        deadline_string = request.POST.get('deadline')
        if deadline_string:
            task.deadline = parse_datetime(deadline_string)
        else:
            task.deadline = None
        task.completed = 'completed' in request.POST
        task.save()
        return redirect('task_list')

    return render(request, 'update_task.html', {'task': task})

def toggle_task_completion(request, task_id):
    task = ToDo.objects.get(id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')
