from django.views.decorators.csrf import csrf_exempt
from django.http import FileResponse, Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from random import randint
from django.urls import reverse
from django.shortcuts import render

from APP.models import Products, Category, Order
from APP.forms import FormBuyProduct

def index(req):
    return render(req, 'index.html')

def contacts(req):
    return render(req, 'contacts.html') 

def buy(req, key):
    return render(req, 'buy.html', {'form': FormBuyProduct(req.POST)})  

@csrf_exempt
def addOrder(req):
    if req.method == "POST":
        form = FormBuyProduct(req.POST)
        if form.is_valid():
            type = Order(
                    name = req.POST['name'],
                    email = req.POST['email'],
                    phone_number = req.POST['phone_number']
            )
            type.save()
            return HttpResponse("Заказ добавлен")
        else:
            return HttpResponse("Некооректное заполнение формы")
    else:
        form = FormBuyProduct
        type = Order(
                name = req.POST['name'],
                email = req.POST['email'],
                phone_number = req.POST['phone_number']
        )
        type.save()
    return render(req, 'order.html', {'form' : form})

def products_view(req):
    if req.POST:
        if req.POST['name'] == '' or req.POST['category'] == '' or req.POST['brand'] == '' or req.POST['price'] == '' or req.POST['appointment'] == '':
            return HttpResponse('Не все поля были заполнены')
        # Есть ли такая категория? 
        # Если да, то берем эту запись(строку) из базы данных
        try:
            cat = Category.objects.get(name=req.POST['name'])
        # Если нет, то содаем запись с данными имени категории и берем эту запись
        except:
            c = Category(
                name = req.POST['name'],
                img_url = 'APP/img/gotovo.jpg'
            )
            c.save()
            cat = Category.objects.get(name=req.POST['name'])
        # Добавляем товар в БД
        pr = Products(
            name = req.POST['name'],
            category_id = cat.id,
            brand = req.POST['brand'],
            appointment = req.POST['appointment'],
            price = req.POST['price'],
        )
        pr.save()

    if 'category' in req.GET:
        try:
            prods = []
            c = Category.objects.get(name=req.GET.get('category'))
            for cosmetic in Products.objects.all():
                if cosmetic.category_id == c.id:
                    cosmetic.category_name = c.name
                    cosmetic.img = c.img_url
                    prods.append(cosmetic)
            return render(req, 'products.html', {'products' : prods})
        except Exception:
            # raise Http404('Такой категории нет')
            return render(req, 'products.html')

    decorative_cosmetics = Products.objects.all()
    # return HttpResponse('<br>'.join([product.name for product in decorative_cosmetics]))
    for prod in decorative_cosmetics:
        cat = Category.objects.get(id=prod.category_id)
        prod.category_name = cat.name
        prod.img = cat.img_url
    return render(req, 'products.html', {'products' : decorative_cosmetics}) 

def product_view(req, prod_num):
    try:
        prod = Products.objects.get(id=prod_num)
        c = Category.objects.get(id=prod.category_id)
        prod.category_name = c.name
        prod.img = c.img_url
        # return HttpResponse(f'Название: {pr.name}')
        return render(req, 'product.html', {'product' : prod}) 
    except:
        raise Http404('Страница не найдена')
    


#2
def products_by_category_view(req: HttpResponse):
    decorative_cosmetics = Products.objects.all() 
    product_list = (products.to_dict() for products in decorative_cosmetics)
    response = {}
    for product in product_list:
        category = response.get(product['category'])
        category.append(product)

    return JsonResponse(response)

#3

def get_product(id:int):
    decorative_cosmetics = Products.objects.all()
    product_with_id = [products for products in decorative_cosmetics if products.id == id]

    if len(product_with_id) == 0:
        raise Http404()
    
    return product_with_id[0]


def json_product_view(req: HttpResponse, id:int):
    decorative_cosmetics = Products.objects.all()
    # for prod in decorative_cosmetics:
    #     prod = get_product(id)

    #     prod.save_as_json()
    for prod in decorative_cosmetics:
        prod.save_as_json()
    
    return FileResponse(open(f'APP/dumps/{id}.json', 'rb'))

#4
categories_files={
    'люкс': 'APP/media/luxe.jpg',
    'мидл-маркет': 'APP/media/middle_market.jpg',
    'масс-маркет': 'APP/media/mass_market.jpg'
}

def category_image_view(req: HttpResponse, name:str):
    if name not in categories_files.keys():
        raise Http404
    return FileResponse(open(categories_files[name], 'rb'), as_attachment=True)

