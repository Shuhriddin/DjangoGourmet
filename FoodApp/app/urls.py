from django.urls import path
from . import views



urlpatterns = [
    path('index/', views.IndexClassViews.as_view(), name='index'),
    path('details/<int:pk>/', views.DetailClassView.as_view(), name='details'),
    # create food
    path('create/', views.CreateFoodView.as_view(), name='create'),
    # update food
    path('edit/<int:id>/', views.update_food, name='update'),
    # delete food
    path('delete/<int:id>/', views.delete_food, name='delete'),
]