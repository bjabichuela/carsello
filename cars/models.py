from django.db import models

# Create your models here.

from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField

# Create your models here.
class Car(models.Model):

    city_choice = (
        ('Antipolo', 'Antipolo'),
        ('BGC', 'BGC'),
        ('Makati', 'Makati'),
        ('Marikina', 'Marikina'),
        ('Pasig', 'Pasig'),
        ('Quezon City', 'Quezon City'),
        ('San Juan', 'San Juan'),
        ('Taguig', 'Taguig'),
    )

    year_choice = []
    for r in range(2000, (datetime.now().year+1)):
        year_choice.append((r,r))

    features_choices = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )

    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )

    transmission_choices = (
        ('Automatic', 'Automatic'),
        ('Manual', 'Manual'),
        ('Hybrid', 'Hybrid'),
    )

    body_choices = (
        ('SUV', 'SUV'),
        ('Crossover', 'Crossover'),
        ('Sedan', 'Sedan'),
        ('Hatchback', 'Hatchback'),
        ('Coupe', 'Coupe'),
        ('Convertible', 'Convertible'),
        ('Sports', 'Sports'),
        ('Truck', 'Truck'),
        ('Van', 'Van'),
    )

    passengers_choices = (
        ('2', '2'),
        ('4', '4'),
        ('6', '6'),
        ('8', '8'),
        ('10', '10'),
        ('12', '12'),
    )

    fuel_choices = (
        ('Gasoline', 'Gasoline'),
        ('Diesel', 'Diesel'),
        ('Bio-diesel', 'Bio-diesel'),
        ('Ethanol', 'Ethanol'),
    )

    car_title = models.CharField(max_length=255)
    city = models.CharField(choices=city_choice, max_length=100)
    color = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(('year'), choices=year_choice)
    condition = models.CharField(max_length=100)
    price = models.IntegerField()
    description = RichTextField()
    car_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    car_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    features = MultiSelectField(choices=features_choices)
    body_style = models.CharField(choices=body_choices, max_length=100)
    engine = models.CharField(max_length=100)
    transmission = models.CharField(choices=transmission_choices, max_length=50)
    interior = models.CharField(max_length=100)
    miles = models.IntegerField()
    doors = models.CharField(choices=door_choices, max_length=10)
    passengers = models.CharField(choices=passengers_choices, max_length=10)
    vin_no = models.CharField(max_length=100)
    milage = models.IntegerField()
    fuel_type = models.CharField(choices=fuel_choices, max_length=50)
    no_of_owners = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.car_title