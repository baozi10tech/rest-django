from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products.views import ProductViewSet, DesignerView

"""
The DefaultRouter automatically generates these routes for your ProductViewSet
because ModelViewSet (which ProductViewSet inherits from) provides default implementations for all CRUD operations:
list: Handles GET /api/products/ to retrieve all products.
retrieve: Handles GET /api/products/<id>/ to retrieve a single product.
create: Handles POST /api/products/ to create a new product.
update and partial_update: Handle PUT and PATCH to update an existing product.
destroy: Handles DELETE to remove a product.
"""
router = DefaultRouter()
router.register(r"products", ProductViewSet, basename="product")
router.register(r"designer", DesignerView, basename="designer")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
