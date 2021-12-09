from django.contrib import admin

# Register your models here.
from app.models import Recipe, Tag, RecipeTag, RecipeIngredientUnit, Ingredient, Unit

class RecipeIngredientUnitInlineAdmin(admin.TabularInline):
    model = RecipeIngredientUnit
    extra = 0

class RecipeAdmin(admin.ModelAdmin):
    inlines = (RecipeIngredientUnitInlineAdmin, )

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
admin.site.register(Unit)
admin.site.register(Tag)
admin.site.register(RecipeTag)
admin.site.register(RecipeIngredientUnit)
