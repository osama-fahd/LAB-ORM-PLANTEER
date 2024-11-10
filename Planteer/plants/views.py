from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Plant
from .forms import PlantForm

def new_view(request:HttpRequest):
    plant_form = PlantForm()
    
    if request.method == "POST":
        plant_form = PlantForm(request.POST, request.FILES)
        if plant_form.is_valid():
            plant_form.save()
            return redirect('main:home_view')
        else:
            return render(request, "plants/new_plant.html", {"categories": Plant.Category.choices})
    
    return render(request, "plants/new_plant.html", {"categories": Plant.Category.choices})

def detail_view(request: HttpRequest, plant_id:int):
    plant = Plant.objects.get(pk=plant_id)
    
    return render(request, "plants/plant_detail.html", {"plant": plant})

def update_view(request: HttpRequest, plant_id):
    plant = Plant.objects.get(pk=plant_id)
    
    if request.method == "POST":
        plant.name = request.POST["name"]
        plant.about = request.POST["about"]
        plant.used_for = request.POST['used_for']
        plant.category = request.POST['category']
        plant.is_edible = request.POST["is_edible"]
        if 'image' in request.FILES: plant.image = request.FILES["image"]
        plant.save()
        
        return redirect("plants:detail_view", plant_id=plant_id)

    return render(request, "plants/update_plant.html", {"plant": plant, "categories": Plant.Category.choices})

def delete_view(request: HttpRequest, plant_id:int):
    plant = Plant.objects.get(pk=plant_id)
    plant.delete()
    
    return redirect("main:home_view")

def search_view(request: HttpRequest):
    if "search" in request.GET and len(request.GET["search"]) >= 1:
        plant = Plant.objects.filter(name__contains=request.GET["search"])
        
        if "order_by" in request.GET and request.GET["order_by"] == "created_at":
            plant = plant.order_by("-created_at")
    else:
        plant = []
    
    return render(request, "plants/search_plant.html", {"plant": plant})

def all_view(request: HttpRequest):
    
    return render(request, "plants/all_plants.html")
    
     


