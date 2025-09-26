from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ToDoForm
from .models import Todo


def index(request):

    items_list = Todo.objects.order_by('-date')
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    form = ToDoForm()

    page = {
        'forms': form,
        'list': items_list,
        'title': 'TODO'
    }

    return render(request, 'todo/index.html', page)


def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, f'Oops! {item.title} is deleted')
    return redirect('todo')
