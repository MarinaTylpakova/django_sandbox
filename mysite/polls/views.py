from django.shortcuts import render
from django.http import HttpResponse
import os

files = list()


def index(request):

    return HttpResponse('Index')


def is_file(path):
    if os.path.isfile(path):
        files.append(path)
    else:
        is_dir(path)


def is_dir(path):
    if os.path.isdir(path):
        file_temp = os.listdir(path=path)
        for file_name in file_temp:
            path_new = path + '/' + file_name
            is_file(path_new)


def new(request):

    path = "../projects"
    is_file(path)
    return render(request, 'polls/index.html', {'files': files})
