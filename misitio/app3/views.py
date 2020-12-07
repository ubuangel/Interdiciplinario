from django.shortcuts import render

# Create your views here.
from .models import provedor, pedido, producto, Cliente

def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    num_b=pedido.objects.all().count()
    num_Pr=provedor.objects.all().count()
    # Libros disponibles (status = 'a')
  #$  num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_p=producto.objects.count()  # El 'all()' esta implícito por defecto.
    
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={'num_b':num_b,'num_Pr':num_Pr,'num_p':num_p},
    )