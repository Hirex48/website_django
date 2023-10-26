from django.urls import path

from APP.views import *

urlpatterns = [
    path('products/', products_view, name='products'),
    path('products/<prod_num>', product_view),
    path('list/<int:id>', json_product_view, name='json_product_view'),
    path('categories/<str:name>', category_image_view , name='category_image_view'),
    path('', index),
    path('contacts/', contacts),
    path('products/<int:key>/buy/',buy),
    path('order/',addOrder),
]
