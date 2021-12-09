from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView

from app.models import Recipe, Ingredient


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['title'] = "Page principale"
        return result


class RecipeListView(ListView):
    template_name = "recipe_list.html"
    model = Recipe


class IngredientListView(ListView):
    template_name = "ingredient_list.html"
    model = Ingredient

class RecipeDetailView(LoginRequiredMixin, DetailView):
    template_name = "recipe_detail.html"
    model = Recipe

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['ingredients'] = Ingredient.objects.filter(
            recipeingredientunit__recipe__pk=self.object.pk
        )
        return result


class IngredientCreateView(CreateView):
    template_name = "ingredient_create.html"
    model = Ingredient
    fields = ('name_singular', 'name_plural')
    success_url = reverse_lazy('ingredient_list')

class IngredientUpdateView(UpdateView):
    template_name = "ingredient_create.html"
    model = Ingredient
    fields = ('name_singular', 'name_plural')
    success_url = reverse_lazy('ingredient_list')
