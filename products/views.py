from rest_framework.decorators import api_view
from rest_framework import response, status
from .models import Product
from .serializers import ProductSerializer


@api_view(['GET'])
def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True, context={"request": request})
        return response.Response(data=serializer.data, status=status.HTTP_200_OK)
