from django.shortcuts import render, HttpResponseRedirect
from .models import *
from .forms import *
from django.urls import reverse



def base(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data.get('isDone')
            form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    context = {
        'tasks': tasks,
        'form': form,
    }
    return render(request, 'Task/base.html', context=context)



def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



def edit_task(request, id):
    task = Task.objects.get(id=id)
    return render(request, 'Task/edit.html', context={'task': task})



def update_task(request, id):
    task = Task.objects.get(id=id)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('base_url'))
    # print(form.errors)
    return render(request, 'Task/edit.html', context={'task': task})
