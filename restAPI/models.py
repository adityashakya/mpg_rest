from django.db import models

# Create your models here.

model_input_values = {'acceleration': 12,
                      'cylinders': 4,
                      'displacement': 100,
                      'horsepower': 90,
                      'model_year': 70,
                      'origin': 2,
                      'weight': 4321}


class MPG(models.Model):
    acceleration=models.FloatField(default=12)
    cylinders=models.FloatField(default=4)
    displacement=models.FloatField(default=100)
    horsepower=models.FloatField(default=90)
    model_year=models.IntegerField(default=70)
    origin=models.IntegerField(default=2)
    weight=models.FloatField(default=4321)


    def __str__(self):
        return f'Model: {self.model_year}, cylinders: {self.cylinders}'

