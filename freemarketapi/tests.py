from django.test import TestCase
from freemarketapi.models import *


# Create your tests here.


class ModelsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Product.objects.create(title='Simple teapot', price=100.00,
                               quantity=113, description='Simple metal teapot')
        user1 = User.objects.create_user(username='Vasya')
        market_user1 = MarketUser.objects.create(user=user1, phone='+1-111-222-333-111')
        order1 = Order.objects.create(comment='My Lord, give to me Mercedes-Benz', user=market_user1)
        prod2 = Product.objects.create(title='iPhuck', description='Imagined phone', price=500.00,
                                       quantity=30)
        rw_phone1 = Review.objects.create(title='Phone review!', content='iPhuck is amazing',
                                          rating=10, product=prod2)
        rw_phone2 = Review.objects.create(title='Phone rev...', content='Ugly', rating=3, product=prod2)
        ProductPhoto.objects.create(image='', product=prod2)
        order1.product_set.add(prod2)

    @classmethod
    def tearDownClass(cls):
        Product.clean(self=Product)

    @staticmethod
    def testProduct():
        for product in Product.objects.all():
            assert product is not None
            assert product.price > 0
            assert product.title != ''
            for order in product.order.all():
                print(f'Order for product {product}: ', order)

    @staticmethod
    def testOrder():
        from django.db.models import Sum
        summa_query = Product.objects.filter(is_selected=True).annotate(Sum('price'))
        summa = 0
        for item in summa_query.all():
            summa += item.price
        try:
            assert summa == 600.00
        except AssertionError:
            print('Failed. Real sum: ', summa)
