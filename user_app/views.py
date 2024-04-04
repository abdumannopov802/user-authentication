from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .models import Product
from .serializers import UserSerializer

@swagger_auto_schema(method='POST', request_body=UserSerializer)
@api_view(['POST'])
def products_for_user(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            user = request.user
            products = Product.objects.filter(category=user.gender)
            return Response({'products': products})
        else:
            return Response({'error': 'User is not authenticated'}, status=401)
    else:
        return Response({'error': 'Method not allowed'}, status=405)
