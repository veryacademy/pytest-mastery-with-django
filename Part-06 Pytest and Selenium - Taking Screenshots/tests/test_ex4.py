# import pytest
# from core.app1.models import Product
# from django.contrib.auth.models import User

# # from django.core.exceptions import ValidationError

# # @pytest.fixture()
# # def user_1(db):
# #     return User.objects.create_user("test-user")

# # @pytest.mark.django_db
# # def test_set_check_password(user_1):
# #     user_1.set_password("new-password")
# #     assert user_1.check_password("new-password") is True

# # def test_set_check_password1(user_1):
# #     print('check-user1')
# #     assert user_1.username == "test-user"

# # def test_set_check_password2(user_1):
# #     print('check-user2')
# #     assert user_1.username == "test-user"

# # def test_new_user(new_user):
# #     print(new_user.first_name)
# #     assert new_user.first_name == "MyName"

# # def test_new_user(new_user2):
# #     print(new_user2.is_staff)
# #     assert new_user2.is_staff

# # def test_new_user(new_user1):
# #     print(new_user1.username)
# #     assert True


# # def test_product(db, product_factory):
# #     product = product_factory.create()
# #     print(product.description)
# #     assert True


# @pytest.mark.parametrize(
#     "title, category, description, slug, regular_price, discount_price, validity",
#     [
#         ("NewTitle", 1, "NewDescription", "slug", "4.99", "3.99", True),
#         ("NewTitle", 1, "NewDescription", "slug", "", "3.99", False),
#     ],
# )
# def test_product_instance(
#     db, product_factory, title, category, description, slug, regular_price, discount_price, validity
# ):

#     test = product_factory(
#         title=title,
#         category_id=category,
#         description=description,
#         slug=slug,
#         regular_price=regular_price,
#         discount_price=discount_price,
#     )

#     item = Product.objects.all().count()
#     print(test)
#     assert item == validity


# @pytest.mark.parametrize(
#     "title, category, description, slug, regular_price, discount_price, validity",
#     [
#         ("NewTitle", 1, "NewDescription", "slug", "4.99", "3.99", True),
#         ("NewTitle", 1, "NewDescription", "slug", "", "3.99", False),
#     ],
# )
# def test_product_instance(
#     db, product_factory, title, category, description, slug, regular_price, discount_price, validity
# ):

#     test = product_factory(
#         title=title,
#         category_id=category,
#         description=description,
#         slug=slug,
#         regular_price=regular_price,
#         discount_price=discount_price,
#     )

#     item = Product.objects.all().count()
#     print(test)
#     assert item == validity
