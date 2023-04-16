from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .forms import AddDebateForm
from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить Статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]

def index(request):
    debats = Debate.objects.all()

    context = {
        'debats': debats,
        'menu': menu,
        'title': 'Главная Страница',
        'cat_selected': 0,
    }
    return render(request, "debate/index.html", context=context)

def about(request):
    return render(request, "debate/about.html", {'menu': menu, 'title': 'О сайте'})

def addpage(request):
    if request.method == 'POST':
        form = AddDebateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddDebateForm()
    return render(request, 'debate/addpage.html', {'form': form,'menu': menu, 'title': 'Добавление статьи'})

def contact(request):
    return HttpResponse("asdasdasd")

def login(request):
    return HttpResponse("asdasdasdas")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def show_page(request, page_slug):
    debate = get_object_or_404(Debate, slug=page_slug)

    context = {
        'debate': debate,
        'menu': menu,
        'title': debate.title,
        'cat_selected': debate.cat_id,
    }
    return render(request, 'debate/debate.html', context=context)

def show_category(request, cat_id):
    debats = Debate.objects.filter(cat_id = cat_id)

    if len(debats) == 0:
        raise Http404()

    context = {
        'debats': debats,
        'menu': menu,
        'title': 'Categories',
        'cat_selected': cat_id,
    }
    return render(request, 'debate/index.html', context = context)
