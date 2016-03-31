from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
partTypeChoices = (
        ('screen', 'Wyświetlacz'),
        ('sensor', 'Czujnik'),
        ('uc', 'Mikrokontroler'),
        ('other', 'Inne'),
        ('connection', 'Komunikacja'),
        ('resistors', 'Rezystory' ),
        ('motor', 'Silnik'),
        ('board', 'Układy scalone'),
        ('multimedia', 'Media'),
)

class Part( models.Model ):
    partID = models.IntegerField( 
        primary_key = True,
        unique = True,
    )
    partName = models.CharField(_(u"Nazwa"), max_length=200, blank=True)
    partCount = models.PositiveIntegerField(_("Ilość"))
    partDescription = models.TextField(_(u"Opis"), max_length=800)
    partType = models.CharField(_(u"Typ"), max_length=100, choices=partTypeChoices )
    
    def append( self, item ):
        self.picture = item

class PartPicture( models.Model ):
    pictureID = models.IntegerField(
        unique=True,
        primary_key=True,
    )
    picture = models.ImageField( _(u"Zdjęcie" ))
    picLabel = models.CharField( _(u"Etykieta"), max_length=100)


class PartDocuments(models.Model):
    docID = models.IntegerField(
        unique=True,
        primary_key=True,
    )
    docFile = models.FileField()
    docLabel = models.CharField(_(u"Etykieta"), max_length=100)


class part_has_picture(models.Model):
    partID = models.ForeignKey("Part")
    picID = models.ForeignKey("PartPicture")
    

    def __init__( self, partID, picID )



class part_has_document(models.Model):
    partID = models.ForeignKey("Part")
    docID = models.ForeignKey("PartDocuments")
