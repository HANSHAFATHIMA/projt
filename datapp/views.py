from django.shortcuts import redirect, render

from datapp.models import ProductDetails

# Create your views here.
#load addproduct.html page
def addproduct(request):
    return render(request,'addproducts.html')

#enter product details
def add_product_details(request):
    if request.method == 'POST':
        pname=request.POST['product_name']
        des=request.POST['description']
        qty=request.POST['quantity']
        price=request.POST['price']
        
        
        product=ProductDetails(product_name=pname,
                               description=des,
                               quantity=qty,
                               price=price)
    
    
    product.save()
    print("hi")
    return redirect('show_products')

#show product details
def show_products(request):
    products=ProductDetails.objects.all()
    return render(request,'show.html',{'product':products})
#load editing page
def editpage(request,pk):
    products=ProductDetails.objects.get(id=pk)
    return render(request,'edit.html',{'products':products})




#editing
def edit_product_details(request,pk):
    if request.method=='POST':
        products = ProductDetails.objects.get(id=pk)
        products.product_name=request.POST.get('product_name')
        products.description=request.POST.get('description')
        products.quantity=request.POST.get('quantity')
        products.price=request.POST.get('price')
        products.save()
        return redirect('show_products')
    return render(request,'edit.html',{'products':products})

#load delete page
def deletepage(request,pk):
    
    products=ProductDetails.objects.get(id=pk)
    return render(request,'delete.html',{'products':products})
#deleting products
def delete_product(request,pk):
    products=ProductDetails.objects.get(id=pk)
    products.delete()
    return redirect('show_products')
    
    