from django.db import models
from imagekit.models import ProcessedImageField
# from imagekit.processors import ResizeToFill

class Season(models.Model):
    season_name = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.season_name}"

class Product(models.Model):
    product_name = models.CharField(max_length=32)
    price_per_kg = models.FloatField(max_length=10)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    storage_kg = models.FloatField(max_length=32)
    description = models.TextField(max_length=150)
    product_image = ProcessedImageField(upload_to='Product_images/')
    # thumbnail = ProcessedImageField(upload_to='thumbnail',
    #                                        processors=[ResizeToFill(100, 50)],
    #                                        format='JPEG',
    #                                        options={'quality': 60})

    def __str__(self):
        return f"{self.product_name}"