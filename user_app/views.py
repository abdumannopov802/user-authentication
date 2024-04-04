from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema, status
from .models import Product
from .serializers import UserSerializer, ProductSerializer
from .models import *

@swagger_auto_schema(method='GET')
@api_view(['GET'])
def products_for_user(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            user = request.user
            products = Product.objects.all()
            json_products = ProductSerializer(products, many=True)
            return Response(json_products.data, status=status.HTTP_200_OK)
        else:
            products = Product.objects.order_by('-rating')[:1]
            json_products = ProductSerializer(products, many=True)
            return Response(json_products.data, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'request method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@swagger_auto_schema(method='POST', request_body=UserSerializer)
@api_view(['POST'])
def create_user(request):
    if request.method == 'POST':
        new_user = UserSerializer(data=request.data)
        if new_user.is_valid():
            birth_date = new_user.validated_data.get('birth_date')
            category_obj = CustomUser.objects.create(birth_date=birth_date)
            category_obj.save()
            return Response(new_user.data, status=status.HTTP_201_CREATED)
        else:
            return Response(new_user.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"Error": "Invalid request type"}, status=status.HTTP_400_BAD_REQUEST)
    
@swagger_auto_schema(method='POST', request_body=ProductSerializer)
@api_view(['POST'])
def create_product(request):
    if request.method == 'POST':
        new_category = ProductSerializer(data=request.data)
        if new_category.is_valid():
            name = new_category.validated_data.get('name')
            category_obj = Product.objects.create(name=name)
            category_obj.save()
            return Response(new_category.data, status=status.HTTP_201_CREATED)
        else:
            return Response(new_category.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"Error": "Invalid request type"}, status=status.HTTP_400_BAD_REQUEST)