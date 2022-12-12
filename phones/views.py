from django.shortcuts import render, redirect, get_object_or_404
from phones.models import Phone
#
def index(request):
    return redirect('catalog')
#
def show_catalog(request):
    template = 'catalog.html'
    first_scen = request.GET.get('sort')
    if first_scen == "min_price":
        phoness = Phone.objects.order_by('price')
        context = {"phones": phoness}
        return render(request, template, context)
    elif first_scen == "max_price":
        phoness = Phone.objects.order_by('-price')
        context = {"phones": phoness}
        return render(request, template, context)
    elif first_scen == "name":
        phoness = Phone.objects.order_by('name')
        context = {"phones": phoness}
        return render(request, template, context)
    else:
        phoness = Phone.objects.all()
        context = {"phones": phoness}
        return render(request, template, context)
#
def show_product(request, slug):
    any_phone = get_object_or_404(Phone, slug=slug)
    template = 'product.html'
    context = {'phone': any_phone, "donot": "?"}
    return render(request, template, context)
# python manage.py makemigrations
# python manage.py migrate
# python manage.py createsuperuser
# root
# root122@gmail.com
# 1234
#