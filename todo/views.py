from django.shortcuts import render

def current_todos(request):
    return render(request, 'current_todos.html')