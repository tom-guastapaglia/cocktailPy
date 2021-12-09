from django.db import models

# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    summary = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        if self.title != "":
            return f"{self.title}"
        return "? (no title)"

class Ingredient(models.Model):
    name_singular = models.CharField(max_length=200, blank=True, null=True)
    name_plural = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        if self.name_singular != "":
            return f"{self.name_singular}"
        return "? (no name_insgular)"

class Tag(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name or "? (no name) ?"

class RecipeTag(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.recipe} / {self.tag}"

class Unit(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        if self.name != "":
            return f"{self.name}"
        return "? (no name)"

class RecipeIngredientUnit(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    value = models.FloatField(default=1.0)
    unit_is_displayed = models.BooleanField(default=True)

    def __str__(self):
        if self.unit_is_displayed:
            return f"{self.recipe} {self.value} {self.unit} {self.ingredient}"
        return f"{self.recipe} {self.value} {self.ingredient}"

