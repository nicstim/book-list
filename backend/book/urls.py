from django.urls import path, include
from book.views import BookViewSet, ProfileViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register("book", BookViewSet)
router.register("profile", ProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
