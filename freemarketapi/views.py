from rest_framework import permissions
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from freemarketapi.serializers import *


# Create your views here.


class MarketUserViewSet(viewsets.ModelViewSet):
    queryset = MarketUser.objects.all()
    serializer_class = MarketUserSerializer

    class Meta:
        model = MarketUser
        fields = '__all__'

    @action(methods=['get', 'post'], detail=False)
    def register(self):
        from django.core.exceptions import MultipleObjectsReturned
        request = self.request
        user = request.user
        username = user['username']
        passwd = user['password']
        phone = request.query_params.get('phone', None)
        if user and phone:
            queryset = self.queryset
            if queryset.filter(user__email=username, user__password__exact=passwd):
                raise MultipleObjectsReturned
            else:
                MarketUser.objects.create(user=User.objects.create(username=username, password=passwd),
                                          phone=phone)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    class Meta:
        model = Order
        fields = ('id', 'user', 'comment')

    @action(methods=['get'], detail=True)
    def get_order(self):
        request = self.request
        user = request.user
        order = Order.objects.get(user=user)
        try:
            serializer = OrderSerializer(order, many=False)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Order.DoesNotExist:
            serializer = OrderSerializer(data={}, many=False)
            return Response(data=serializer.data, status=status.HTTP_200_OK)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    class Meta:
        model = Product
        fields = ('id', 'title', 'price', 'quantity', 'description', 'order')

    '''
    Allow create new products to only admin personnel
    '''
    def create(self, request: Request, *args, **kwargs):
        user: User = request.user
        if user.is_authenticated and user.is_superuser:
            return super(ProductViewSet, self).create(request, *args, **kwargs)
        else:
            return Response(data={}, status=status.HTTP_403_FORBIDDEN)

    '''
    Allow update info at product to only admin personnel
    '''
    def update(self, request: Request, *args, **kwargs):
        user: User = request.user
        if user.is_authenticated and user.is_superuser:
            return super(ProductViewSet, self).create(request, *args, **kwargs)
        else:
            return Response(data={}, status=status.HTTP_403_FORBIDDEN)
