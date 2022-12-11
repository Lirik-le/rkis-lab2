from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'books', views.BookAPIView)

urlpatterns = [
    path('', include(router.urls)),
    # path('books_list', views.BookAPIView.as_view({'get': 'list'})),
    # path('book_create', views.BookAPIView.as_view({'post': 'create'})),
    # path('book_detail/<int:pk>', views.BookAPIView.as_view({'get': 'retrieve'})),
    # path('book_update/<int:pk>', views.BookAPIView.as_view({'post': 'update'})),
    # path('book_delete/<int:pk>', views.BookAPIView.as_view({'get': 'destroy'})),
]

