from django.shortcuts import render
from .models import Category, Author, Recipe
from django.views.generic import ListView, DetailView
from .models import Recipe
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


def index(request):
    text_head = 'Here you will find my favourite recipes'
    recipes = Recipe.objects.all()
    num_recipes = Recipe.objects.all().count()
    authors = Author.objects
    num_authors = Author.objects.count()
    context = {'text_head': text_head,
               'recipes': recipes, 'num_recipes': num_recipes,
               'authors': authors, 'num_authors': num_authors}
    return render(request, 'myapp/index.html', context)


class RecipeListView(ListView):
    model = Recipe
    context_object_name = 'recipes'


class RecipeDetailView(DetailView):
    model = Recipe
    context_object_name = 'recipe'


class AuthorListView(ListView):
    model = Author


def contact(request):
    text_head = 'Contact details'
    name = 'Mariia G'
    tel = '987-65-43-21'
    email = 'maria@mail.ru'
    context = {'text_head': text_head, 'name': name, 'tel': tel, 'email': email}
    return render(request, 'myapp/contact.html', context)


def edit_recipes(request):
    recipe = Recipe.objects.all()
    context = {'recipe': recipe}
    return render(request, "myapp/edit_recipes.html", context)


class RecipeCreate(CreateView):
    model = Recipe
    fields = '__all__'
    success_url = reverse_lazy('edit_recipes')


class RecipeUpdate(UpdateView):
    model = Recipe
    fields = '__all__'
    success_url = reverse_lazy('edit_recipes')


class RecipeDelete(DeleteView):
    model = Recipe
    success_url = reverse_lazy('edit_recipes')