# Generated by Django 5.1.1 on 2024-10-02 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodApp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_food', models.CharField(max_length=100)),
                ('type_food', models.CharField(max_length=200)),
                ('price_food', models.FloatField(default=45.0)),
                ('image_food', models.ImageField(default='pic.jpg', upload_to='food_image')),
                ('description_food', models.TextField()),
            ],
        ),
    ]
