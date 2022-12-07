from django.db import models
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File

# Create your models here.
class Bar_code(models.Model):
    name = models.CharField(max_length=50)
    bar_code = models.ImageField(upload_to='all_image_code/barcodes_images/', blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        COD128 = barcode.get_barcode_class('code128')
        rv = BytesIO()
        code = COD128(f'{self.name}', writer=ImageWriter()).write(rv)
        self.bar_code.save(f'{self.name}.png', File(rv), save=False)
        return super().save(*args, **kwargs)