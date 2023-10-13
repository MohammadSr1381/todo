from django.shortcuts import render , get_object_or_404
from django.shortcuts import HttpResponse , redirect
from .models import Task



def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')

#for moving tasks from undone list to done
def mark_as_done(request , pk):
    task = get_object_or_404(Task,pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

#for editing tasks
def edit_task(request , pk):
    get_task = get_object_or_404(Task , pk=pk)
    if request.method == "POST":
        new_task = request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect("home")
    else :
        context = {
            'get_task' : get_task
        }
        return render(request,'edit_task.html' , context)

#for deleting task from undone list
def delete_task(request , pk):
    task = get_object_or_404(Task , pk = pk)
    task.delete()
    return redirect('home')
