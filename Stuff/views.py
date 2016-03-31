from django.shortcuts import render

from .forms import NewPart
from .forms import NewPartPicture

from .models import Part
from .models import PartPicture 
from .models import part_has_picture

# Create your views here.
 
def home(request):
    return render(request, 'Stuff/home.html', {"title":"HOME"} )


def settings(request):
    form = NewPart()

    if request.method == "POST":
        form = NewPart( request.POST )
        picture = NewPartPicture( request.POST, request.FILES )
        if form.is_valid():
            partInstance = form.save()
            
    #if request.method == "POST":
    #    pictures = NewPartPicture( request.POST, request.FILES )
    #    if pictures.is_valid():
    #        pictures.save()
    return render(request, 'Stuff/settings.html', {"form":form, "title":'Dodaj część' } )


def showAll( request ):
    parts =  Part.objects.all()
    pictures = PartPicture.objects.all() 
    pikczure = []
    stuffs = ()
    for part in parts:
        for picture in pictures:
            if part.partID == picture.pictureID:
                part.append( picture.picture )
    print( list(parts) ) 
    return render( request, "Stuff/listAll.html", {"content":parts, "pikczure":pikczure} )


def devForm( request ):
    return render( request, "Stuff/devForm.html", {} )
