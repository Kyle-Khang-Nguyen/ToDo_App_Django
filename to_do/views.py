from django.shortcuts import render, redirect
from .models import ToDo

# Create your views here.
def task_list(request):
    tasks = ToDo.objects.all()
    return render(request, 'to_do.html', {'tasks': tasks})

def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        deadline = request.POST.get('deadline') or None

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
        task.deadline = request.POST.get('deadline')
        task.completed = 'completed' in request.POST
        task.save()
        return redirect('task_list')

    return render(request, 'update_task.html', {'task': task})
