from django.core.management.base import BaseCommand
from django.utils.text import slugify
from store.models import Category, Product
import random

class Command(BaseCommand):
    help = "Seed categories and products for Home Furnishing store"

    def handle(self, *args, **kwargs):

        categories = {
            "Curtains": [
                ("Blackout Curtains", 1499),
                ("Sheer Curtains", 999),
                ("Printed Curtains", 1299),
            ],
            "Bedsheets": [
                ("Cotton Double Bedsheet", 1799),
                ("King Size Bedsheet", 1999),
                ("Printed Bedsheet Set", 1599),
            ],
            "Cushion Covers": [
                ("Velvet Cushion Cover", 499),
                ("Printed Cushion Cover", 399),
                ("Embroidered Cushion Cover", 699),
            ],
            "Sofa Covers": [
                ("Elastic Sofa Cover", 2499),
                ("Luxury Sofa Cover", 2999),
            ],
            "Carpets & Rugs": [
                ("Handwoven Carpet", 4999),
                ("Modern Area Rug", 3499),
            ],
        }

        for category_name, products in categories.items():
            category, created = Category.objects.get_or_create(
                name=category_name,
                slug=slugify(category_name)
            )

            for product_name, price in products:
                Product.objects.get_or_create(
                    title=product_name,
                    slug=slugify(product_name),
                    category=category,
                    defaults={
                        "price": price,
                        "description": f"Premium quality {product_name.lower()} for your home.",
                        "is_active": True,
                    }
                )

        self.stdout.write(self.style.SUCCESS("✅ Home Furnishing data seeded successfully"))
