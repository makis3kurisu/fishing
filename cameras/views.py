from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Camera

@csrf_exempt
def add_camera(request):
    if request.method == 'POST':
        name = request.POST['name']
        url = request.POST['url']
        latitude = request.POST['latitude']
        longitude = request.POST['longitude']
        Camera.objects.create(name=name, url=url, latitude=latitude, longitude=longitude)
        return redirect('admin:cameras_camera_changelist')
    return render(request, 'admin/map_with_controls.html')

def map_view(request):
    cameras = Camera.objects.all()
    return render(request, 'map.html', {'cameras': cameras})
