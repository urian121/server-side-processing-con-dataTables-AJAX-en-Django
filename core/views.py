from django.shortcuts import render

from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import Producto

def productos_list(request):
    return render(request, 'core/index.html')

def productos_ajax(request):
    draw = request.GET.get('draw')
    start = int(request.GET.get('start', 0))
    length = int(request.GET.get('length', 10))
    search_value = request.GET.get('search[value]', '')

    queryset = Producto.objects.all()

    if search_value:
        queryset = queryset.filter(nombre__icontains=search_value)

    total = queryset.count()

    paginator = Paginator(queryset, length)
    page_number = start // length + 1
    page = paginator.get_page(page_number)

    data = []
    for producto in page:
        data.append([
            producto.id,
            producto.nombre,
            str(producto.precio)
        ])

    return JsonResponse({
        'draw': draw,
        'recordsTotal': total,
        'recordsFiltered': total,
        'data': data,
    })

