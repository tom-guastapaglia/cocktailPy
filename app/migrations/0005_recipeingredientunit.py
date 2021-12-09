# Generated by Django 3.2.9 on 2021-12-07 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_recipetag_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeIngredientUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField(default=1.0)),
                ('unit_is_displayed', models.BooleanField(default=True)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ingredient')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.recipe')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.unit')),
            ],
        ),
    ]