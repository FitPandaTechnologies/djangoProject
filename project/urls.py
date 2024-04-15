from django.contrib import admin
from django.urls import path

from app.views import BookPriceView, list_authors

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authors/', list_authors, name='authors-list'),

    path('api/v1/authors/', list_authors, name='authors-list-api'),
    path('books/<int:pk>/price/', BookPriceView.as_view(), name='book-price'),
]
