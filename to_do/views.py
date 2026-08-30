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
        deadline = request.POST.get('deadline')

        ToDo.objects.create(title=title, description=description, deadline=deadline)
        return redirect('task_list')

    return render(request, 'create_task.html')

def delete_task(request, task_id):
    task = ToDo.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')
