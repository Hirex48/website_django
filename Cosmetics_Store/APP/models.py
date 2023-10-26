
import json
from django.db import models

class Products(models.Model):
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['-name', 'price']
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, null=True, verbose_name = 'Название')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name = 'Категория')
    price = models.IntegerField(verbose_name = 'Стоимость')
    brand = models.CharField(max_length=200, null=True, verbose_name = 'Бренд')
    appointment = models.CharField(max_length=200, null=True, verbose_name = 'Назначение')

    def __str__(self):
        return self.name
    
    def to_dict(self) -> dict:
        return {
        'ID' : self.id,
        'name' : self.name,
        'category_id' : self.category_id,
        'category_name' : Category.objects.get(id=self.category_id).name,
        'brand' : self.brand,
        'appointment' : self.appointment,
        'price' : self.price
        }
    
    def save_as_json(self):
        with open(f'APP/dumps/{self.id}.json', 'w+') as file:
            json.dump(self.to_dict(), file)

    
class Category(models.Model): 
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, null=True, verbose_name='Название')
    img_url = models.CharField(max_length=200, null=True, verbose_name='Путь до изображения')
    def __str__(self):
        return self.name
    
    
class Order(models.Model):
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, null=False)
    email = models.EmailField(max_length=200, null=False)
    phone_number = models.CharField(max_length=200, null=False)