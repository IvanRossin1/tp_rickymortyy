# capa de vista/presentación

from django.shortcuts import redirect, render
from .layers.services import services
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from .layers.services.services import getAllImages

from .layers.transport import transport

from django.core.paginator import Paginator


def index_page(request):
    return render(request, 'index.html')

# esta función obtiene 2 listados que corresponden a las imágenes de la API y los favoritos del usuario, y los usa para dibujar el correspondiente template.
# si el opcional de favoritos no está desarrollado, devuelve un listado vacío.
def home(request):
    images = [] # lista de imagenes de la api
    
    images = transport.getAllImages() # obtiene las imagenes desde transport
    
    favourite_list = [] #lista favoeritos

    return render(request, 'home.html', { 'images': images, 'favourite_list': favourite_list })


# def home(request, page=1):
#     images = services.getAllImages()
    
#     paginator = Paginator(images, per_page=9)
    
#     page_object = paginator.get_page(page)
#     context = {'page_object': page_object}
    
#     return render(request, 'home.html', context)


def search(request):
    search_msg = request.POST.get('query', '') #agarra el texto ingresado. si no hay nada, devuelve una cadena vacia

    # si el texto ingresado no es vacío, trae las imágenes y favoritos desde services.py, y luego renderiza el template (similar a home).
    if (search_msg != ''):
        images = services.getAllImages(search_msg) # obtiene las imagenes de la api, a traves del objeto images
        
        return render(request, 'home.html', {'images': images}) 
    else:
        return redirect('home') # si esta vacio redirige al home


# Estas funciones se usan cuando el usuario está logueado en la aplicación.
@login_required
def getAllFavouritesByUser(request):
    favourite_list = []
    return render(request, 'favourites.html', { 'favourite_list': favourite_list })

@login_required
def saveFavourite(request):
    pass

@login_required
def deleteFavourite(request):
    pass

@login_required
def exit(request):
    pass