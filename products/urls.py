from django.urls import path
from .views import product_list, add_review, product_details


urlpatterns = [
    path("", product_list, name="product_list"),
    path("<int:id>", product_details, name="product_details"),
    path("add/", add_review, name="add_review"),
]
