# Generated by Django 4.1.3 on 2022-11-16 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('detail', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True)),
                ('name_abbrev', models.CharField(blank=True, max_length=60)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='ingredient',
        ),
        migrations.AddField(
            model_name='ingredient',
            name='recipe',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='recipes_app.recipe'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='amount_number',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Amount',
        ),
        migrations.AddField(
            model_name='ingredient',
            name='food',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='recipes_app.food'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='recipes_app.unit'),
        ),
    ]
