from django.shortcuts import render, redirect
from .models import Product, Review


# Create your views here.
def product_list(request):
    products = Product.objects.all()
    context = {
        "products": products,
    }
    return render(
        request,
        'products/products.html',
        context
        )


def product_details(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        "product": product,
        "reviews": product.reviews
    }
    return render(
        request,
        "products/product_details.html",
        context
    )


def add_review(request):
    if request.method == "POST":
        product_id = request.POST.get("product")
        author = request.POST.get("author")
        text = request.POST.get("review-text")
        rating = request.POST.get("rating")

        product = Product.objects.get(id=product_id)
        # Я тут з try та except не буду заморачуватися
        Review.objects.create(
            product=product,
            author=author,
            text=text,
            rating=rating,
        )
        return redirect("product_list")
    else:
        return render(
            request,
            "products/add_review.html"
        )
