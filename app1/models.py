from django.db import models
from django.utils.timezone import now

class cardealer(models.Model):
    name= models.CharField(max_length=100)
    # experience = models.IntegerField()
    detail = models.TextField()
    def __str__(self):
        return self.name


class carmake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class carmodel(models.Model):
    name = models.CharField(max_length=100)
    year = models.DateField()
    cartype= models.CharField(max_length=200)
    dealer = models.ForeignKey(cardealer, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class carreview(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField()
    com = models.ForeignKey(carmodel, on_delete = models.CASCADE)


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
