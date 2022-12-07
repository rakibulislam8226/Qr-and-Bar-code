from django.db import models
from io import BytesIO
from PIL import Image
import qrcode
from django.core.files import File

class QrCode(models.Model):
    name = models.CharField(max_length=50)
    qr_code = models.ImageField(upload_to='all_image_code/qr_codes_images/', blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make("FLAT50")
        canvas = Image.new('RGB', (290, 290), 'white')
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.name}.png'
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)