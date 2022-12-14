from django.shortcuts import render
from .models import Photo
from django.views.decorators.csrf import csrf_protect
# Create your views here.
# 

@csrf_protect
def index(request):
    if request.method == 'POST':
        new_photo = Photo(
            file = request.FILES['img']
        )
        new_photo.save()
        return render(request, 'index.html', {'new_url': str('https://photosharing.up.railway.app'+new_photo.file.url)})
    else:
        return render(request, 'index.html')
