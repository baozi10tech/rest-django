from rest_framework import viewsets, status
from rest_framework.viewsets import ViewSet
from rest_framework.request import Request
from rest_framework.response import Response
from products.models import Product, Designer
from products.serializers import ProductSerializer, DesignerSerializer
from typing import Optional


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class DesignerView(ViewSet):
    def list(self, request: Request) -> Response:
        name: Optional[str] = request.query_params.get("name", None)
        if name:
            designers = Designer.objects.filter(name__icontains=name)
        else:
            designers = Designer.objects.all()

        serializer = DesignerSerializer(designers, many=True)
        return Response(serializer.data)

    def create(self, request: Request) -> Response:
        serializer = DesignerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
