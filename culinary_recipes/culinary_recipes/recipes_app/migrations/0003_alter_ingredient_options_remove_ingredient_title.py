# Generated by Django 4.1.3 on 2022-11-16 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes_app', '0002_food_unit_remove_recipe_ingredient_ingredient_recipe_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingredient',
            options={'ordering': ['order_index', 'id']},
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='title',
        ),
    ]
