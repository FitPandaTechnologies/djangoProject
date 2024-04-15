from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Author, Stock
from .serializers import AuthorSerializer


def list_authors(request):
    authors = Author.objects.all()
    return render(request, 'authors-list.html', {'authors': authors})


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookPriceView(APIView):
    def get_object(self, pk):
        try:
            return Stock.objects.get(book__pk=pk)
        except Stock.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        stock = self.get_object(pk)
        return Response({
            'book_title': stock.book.title,
            'price_excl_vat': stock.price_excl_vat,
            'vat_percentage': stock.vat_percentage,
            'price_incl_vat': stock.price_incl_vat
        })
