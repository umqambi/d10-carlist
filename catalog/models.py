from django.db import models

class Car(models.Model):
    TRANSMISSIONS = [
        (1,'Механика'),
        (2, 'Автомат'),
        (3, 'Робот'),
    ]

    brand = models.CharField(max_length=50)                          #производитель (BMW, Audi, Tesla и т.д.) (CharField)
    car_model = models.CharField(max_length=30)                      #модель авто (S, TT, X6 и т.д.) (CharField)
    year = models.IntegerField()                        #год выпуска (IntegerField)
    transmission = models.SmallIntegerField(
        choices=TRANSMISSIONS,
        verbose_name="Коробка передач"
    )                                                   #коробка передач (SmallIntegerField with choices "механика", "автомат", "робот")
    color = models.CharField(max_length=30)                          #цвет
