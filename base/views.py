from multiprocessing import context
from django.shortcuts import render

# Create your views here.

posts = [
    {'id': 1, 'name': 'Lets learn Python!'},
    {'id': 2, 'name': 'Design with me'},
    {'id': 3, 'name': 'Front End Developers'},
]


def home(request):
    context = {'posts': posts}
    return render(request, 'base/home.html', context)


def post(request, pk):
    room = None
    for i in posts:
        if i['id'] == int(pk):
            room = i
    
    context = {'room': room}
    return render(request, 'base/post.html', context)
