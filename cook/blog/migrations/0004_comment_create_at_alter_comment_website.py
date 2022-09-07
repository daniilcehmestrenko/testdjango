# Generated by Django 4.1.1 on 2022-09-07 10:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_recipe_directions_alter_recipe_ingredients_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='create_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='comment',
            name='website',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]