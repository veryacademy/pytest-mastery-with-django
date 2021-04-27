import factory
from faker import Faker
fake = Faker()

from django.contrib.auth.models import User
from core.app1 import models


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = fake.name()
    is_staff = 'True'


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Category

    name = 'django'


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Product

    title = 'product_title'
    category = factory.SubFactory(CategoryFactory)
    description = fake.text()
    slug = 'product_slug'
    regular_price = '9.99'
    discount_price = '4.99'