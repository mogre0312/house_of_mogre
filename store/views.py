from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product
from django.db.models import Q

def home(request):
    featured = Product.objects.filter(is_active=True).order_by("-created")[:20]
    categories = Category.objects.all()
    return render(request, "home.html", {"featured": featured, "categories": categories})

def category_list(request):
    categories = Category.objects.all()
    return render(request, "category_list.html", {"categories": categories})

def category_detail(request, slug):
    cat = get_object_or_404(Category, slug=slug)
    products = cat.products.filter(is_active=True)
    return render(request, "category_detail.html", {"category": cat, "products": products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    # main image:
    images = product.images.all()
    return render(request, "product_detail.html", {"product": product, "images": images})

def search(request):
    q = request.GET.get("q", "")
    results = Product.objects.none()
    if q:
        results = Product.objects.filter(Q(title__icontains=q) | Q(description__icontains=q), is_active=True)
    return render(request, "search.html", {"q": q, "results": results})

def add_to_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    cart = request.session.get("cart", {})
    cart[str(product.id)] = cart.get(str(product.id), 0) + 1
    request.session["cart"] = cart
    return redirect("store:cart")

def remove_from_cart(request, product_id):
    cart = request.session.get("cart", {})
    product_id = str(product_id)

    if product_id in cart:
        del cart[product_id]

    request.session["cart"] = cart
    return redirect("store:cart")

def cart_detail(request):
    cart = request.session.get("cart", {})
    cart_items = []
    total = 0

    for product_id, qty in cart.items():
        product = Product.objects.filter(id=product_id).first()

        if not product:
            continue 

        subtotal = product.price * qty
        total += subtotal

        cart_items.append({
            "product": product,
            "qty": qty,
            "subtotal": subtotal
        })

    return render(request, "cart.html", {
        "cart_items": cart_items,
        "total": total,
    })

def increase_qty(request, product_id):
    cart = request.session.get("cart", {})

    pid = str(product_id)

    if pid in cart:
        cart[pid] += 1

    request.session["cart"] = cart
    return redirect("store:cart")


def decrease_qty(request, product_id):
    cart = request.session.get("cart", {})
    pid = str(product_id)

    if pid in cart:
        if cart[pid] > 1:
            cart[pid] -= 1

    request.session["cart"] = cart
    return redirect("store:cart")






