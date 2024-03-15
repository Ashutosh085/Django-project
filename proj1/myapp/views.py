from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User
from .models import Product

# Create your views here.
def myapp(request):
    myusers =User.objects.all().values()
    template = loader.get_template('index.html')
    #return loader.get_template('index.html).render()
    myproducts=Product.objects.all().values
    context = {
        'myuserlist': myusers,
        'myproductslist': myproducts
        # 'variable1' : "sdfg"
    }
    return HttpResponse(template.render(context, request))

def prod_details(request, id):
    product=Product.objects.get(id=id)
    context={
        'product':product
    }
    template=loader.get_template('prod_details.html')
    return HttpResponse(template.render(context, request))


def userLogin(request):
    return HttpResponse("The login page is yet to be filled")