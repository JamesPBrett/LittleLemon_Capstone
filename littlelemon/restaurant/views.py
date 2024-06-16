from django.shortcuts import render
from rest_framework import generics
from .models import Menu
from .serializers import MenuSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})


# View for GET and POST requests for the list of menu items
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


# View for GET, PUT, and DELETE requests for a single menu item
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer