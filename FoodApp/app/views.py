from typing import Any
from django.shortcuts import render, redirect
from .models import FoodApp
from .forms import CreateFood
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
# search
from django.db.models import Q
from django.db.models.query import QuerySet
from django.core.paginator import Paginator
# Create your views here.


# index ===========================================================================================================================
def get_index(request):
    food = FoodApp.objects.all()
    # Paginator
    paginator = Paginator(food, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'food': food,
        'page_obj': page_obj,
    }
    return render(request, 'food/index.html', context)

class IndexClassViews(ListView):
    model = FoodApp
    template_name = 'food/index.html'
    context_object_name = 'food'

    paginate_by = 4

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            multipy_q = Q(Q(name_food__icontains=q) | Q(type_food__icontains=q) | Q(price_food__icontains=q))
            queryset = queryset.filter(multipy_q)
        return queryset


# detail ===========================================================================================================================
def details(request, my_id):
    food = FoodApp.objects.get(pk=my_id)
    context = {
        'food': food
    }
    return render(request, 'food/details.html', context)


class DetailClassView(DetailView):
    model = FoodApp
    template_name = 'food/details.html'

# create ===========================================================================================================================

def create_food(request):
    form = CreateFood(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'food/create_food.html', {'form': form})


# this class based view for create food
class CreateFoodView(CreateView):
    model = FoodApp
    fields = "__all__"
    template_name = 'food/create_food.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user

        return super().form_valid(form)

# edit ===========================================================================================================================

def update_food(request, id):
    food = FoodApp.objects.get(id=id)
    form = CreateFood(request.POST or None, instance=food)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'food/create_food.html', {'food': food, 'form': form})

# delete ===========================================================================================================================
def delete_food(request, id):
    food = FoodApp.objects.get(id=id)
    if request.method == "POST":
        food.delete()
        return redirect('index')
    return render(request, 'food/delete.html', {'food': food})