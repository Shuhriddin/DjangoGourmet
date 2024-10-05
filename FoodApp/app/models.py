from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class FoodApp(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # food qo`shishda default=1 bo`lganligi sabab Shuxa ni tanlab ko`rsatadi
    name_food = models.CharField(max_length=100)
    type_food = models.CharField(max_length=200)
    price_food = models.FloatField(default=45.000)
    image_food = models.ImageField(upload_to='food_image', default='pic.jpg')
    description_food = models.TextField()

    def __str__(self) -> str:
        return self.name_food
    
    def get_absolute_url(self):
        return reverse('details', kwargs={'pk': self.pk})