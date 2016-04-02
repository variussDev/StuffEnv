from django.shortcuts import render

from .forms import NewPart
from .forms import NewPartPicture
from .forms import Part_to_picture_test

import Stuff.models  as table
from .models import Part
from .models import PartPicture 
from .models import Part_has_picture

# Create your views here.
 
def home(request):
    return render(request, 'Stuff/home.html', {"title":"HOME"} )


def settings(request):
    form = NewPart()

    if request.method == "POST":
        form = NewPart( request.POST )
        #picture = NewPartPicture.create( request.FILES, "fileeeee" )
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
    form = NewPartPicture()
    if request.method == "POST":
        form = NewPartPicture( request.POST, request.FILES )
        if form.is_valid():
            picture = form.save()
    return render( request, "Stuff/devForm.html", {"form":form} )

def detailedList( request, part ):
    parts = Part.objects.filter( partType = part )
    print( 'znalezione czesci' )
    print ( parts )
    partsID = []
    for part in parts:
        partsID.append( part.partID )
    
    partsWithPictures = Part_has_picture.objects.filter( part =  parts )
    print('---------------------------')
    print(  partsWithPictures )
    print('---------------------------')
    return render( request, "Stuff/detailedList.html", {"title":"Części", "parts":parts, "partsWithPictures":partsWithPictures} )


def edit( request, id ):
    part = Part.objects.get( partID=id )
    form = NewPartPicture()
    print( 'id elementu:::' + str( part.partID ) )
    if request.method == "POST":
        form = NewPartPicture( request.POST, request.FILES )
        if form.is_valid():
            picture = form.save()
            rel = table.Part_has_picture.create( part, picture )
            rel.save()
            print( rel.pic )
            print( 'picture id:::' + str( picture.pictureID ) ) 
    return render( request, "Stuff/editPart.html", {"part": part, "form":form})
