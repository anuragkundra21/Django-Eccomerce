from django.shortcuts import render
from store.models import Product,Order
from math import ceil
# Create your views here.
def home(request):
    return render(request,'store/home.html')

def index(request):
    products = Product.objects.all()
    print(products)
    #n = len(products)
    #nSlides= n//4 + ceil((n/4)-(n//4))
    allProds=[]
    catProds=Product.objects.values('category','id')
    cats ={item['category'] for item in catProds}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides= n//4 + ceil((n/4)-(n//4))
        allProds.append([prod,range(1,nSlides),nSlides])
    #params={'no_of_slides':nSlides,'range':range(1,nSlides),'product':products}
    #allProds=[[products,range(1,nSlides),nSlides],[products,range(1,nSlides),nSlides]]
    params={'allProds':allProds}
    return render(request,'store/index.html',params)
def about(request):
    return render(request,'store/about.html')
def search(request):
    return HttpResponse('Search')
def product(request,myid):
    product = Product.objects.filter(id=myid)
    return render(request,'store/product.html',{'product':product[0]})
def register(request):
    return HttpResponse('register')
def login(request):
    return HttpResponse('Login')
def checkout(request):
    if request.method=='POST':
        items_json=request.POST.get('itemsjson',"")
        amount=request.POST.get('amount',"")
        name=request.POST.get('name',"")
        email=request.POST.get('email',"")
        address=request.POST.get('address1',"")+ "" +request.POST.get('address2',"")
        city=request.POST.get('city',"")
        state=request.POST.get('state',"")
        zip=request.POST.get('zip',"")
        phone=request.POST.get('phone',"")
        order=Order(items_json=items_json,name=name,email=email,address=address,city=city,state=state,zip=zip,phone=phone,amount=amount)
        order.save()
        thank=True
        id=order.order_id
        return render(request,'store/checkout.html',{'thank':thank,'id':id})
    return render(request,'store/checkout.html')
