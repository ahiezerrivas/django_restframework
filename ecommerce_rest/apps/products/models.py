from django.db import models
from simple_history.models import HistoricalRecords

from apps.base.models import BaseModel
# Create your models here.

class MeasureUnit(BaseModel):

    description = models.CharField('Descripcion', max_length=50, blank= False, null= False, unique = True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Unidad de Medida'
        verbose_name_plural = 'Unidades de Medidas'

    def __str__(self):
        return self.description
    
class CategoryProduct(BaseModel):


    description = models.CharField('Descripcion', max_length=50, blank= False, null= False, unique = True)
    
    historical = HistoricalRecords()


      

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
    class Meta:
        verbose_name = "CategoryProduct"
        verbose_name_plural = "CategoryProducts"

    def __str__(self):
        return self.description

class Indicator(BaseModel):

    descount_value = models.PositiveSmallIntegerField(default=0)
    historical = HistoricalRecords()


      

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = "Indicator"
        verbose_name_plural = "Indicators"

    def __str__(self):
        return f'Oferta de la categoria {self.category_product} : {self.descount_value}%'

class Product(BaseModel):

    name= models.CharField('Nombre de Producto', max_length=150, unique= True, blank=False, null= False)
    description = models.TextField('Descripcion de Producto', blank= False, null= False)
    image = models.ImageField('Imagen del producto', upload_to='products/', blank=True,null=True)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE,verbose_name='Unidad de medida',null=True)
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE,verbose_name='Categoria de Productos', null=True)
    historical = HistoricalRecords()


      

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.name
