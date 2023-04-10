from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import BookModel
from .serializers import BookSerializers
from rest_framework.response import Response
from django.db.models import Min, Max
# Create your views here.



def home_view(request):
    min_value = BookModel.objects.aggregate(Min('price'))
    max_value = BookModel.objects.aggregate(Max('price'))

    context = {
         'min_value':min_value,
         'max_value':max_value
    }
    return render(request,'home.html', context)

# only make api code here 
@api_view(['GET'])  # USE TO MAKE api for a particular method where i used to make get method only 
def Get_View(request):
    books = BookModel.objects.all() 
    price = request.GET.get('price')

    if price:
        books = books.filter(price__lte = price) # for price search 

    name = request.GET.get('name')  # get the name value 
   
    if name:
        books = books.filter(name__contains = name)
    
    serializer = BookSerializers(books, many = True)   #used many = True becase i want all the data to the files 
    
    if serializer.data:
        return Response(serializer.data)
    else:

    
        return Response (serializer.data)  # import serailizer response to redirect  to response  

