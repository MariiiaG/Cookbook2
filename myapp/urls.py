from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipes/', views.RecipeListView.as_view(), name='recipes-list'),
    path('recipes/<int:pk>/', views.RecipeDetailView.as_view(), name='recipe-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors-list'),
    path('contact/', views.contact, name='contact'),
    path('edit_recipes/', views.edit_recipes, name='edit_recipes'),
    path('recipe/create/', views.RecipeCreate.as_view(), name='recipe_create'),
    path('recipe/update/<int:pk>/', views.RecipeUpdate.as_view(), name='recipe_update'),
    path('recipe/delete/<int:pk>/', views.RecipeDelete.as_view(), name='recipe_delete'),
]