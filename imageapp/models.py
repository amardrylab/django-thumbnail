from django.db import models
from PIL import Image
from .my_app_settings import THUMB_SIZE
import os.path
from io import BytesIO
from django.core.files.base import ContentFile

# Create your models here.

class Hotel(models.Model):
    name=models.CharField(max_length=50)
    hotel_Main_Img=models.ImageField(upload_to='images/')
    thumbnail=models.ImageField(upload_to='thumbs/', editable=False)

    def save(self, *args, **kwargs):
        if not self.make_thumbnail():
            raise Exception('Could not make thumbnail')
        super(Hotel, self).save(*args, **kwargs)

    def make_thumbnail(self):
        image=Image.open(self.hotel_Main_Img)
        image.thumbnail(THUMB_SIZE, Image.ANTIALIAS)

        thumb_name, thumb_extension=os.path.splitext(self.hotel_Main_Img.name)
        thumb_extension=thumb_extension.lower()
        thumb_filename=thumb_name + '_thumb'+thumb_extension

        if thumb_extension in ['.jpg', '.jpeg']:
            FTYPE='JPEG'
        elif thumb_extension =='.gif':
            FTYPE='GIF'
        elif thumb_extension == '.png':
            FTYPE='PNG'
        else:
            return False

        #save thumbnail to in-memory file a StringIO
        temp_thumb=BytesIO()
        image.save(temp_thumb, FTYPE)
        temp_thumb.seek(0)

        #set save=False, otherwise it will run in infinite loop
        self.thumbnail.save(thumb_filename, ContentFile(temp_thumb.read()), save=False)
        temp_thumb.close()
        return True
