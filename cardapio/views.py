from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Categoria, ItemCardapio


def cardapio_home(request):
    """Página principal com todos os itens agrupados por categoria."""
    categorias = Categoria.objects.prefetch_related(
        'itens'
    ).filter(itens__disponivel=True).distinct()

    destaques = ItemCardapio.objects.filter(
        destaque=True,
        disponivel=True
    )

    return render(request, 'cardapio/home.html', {
        'categorias': categorias,
        'destaques': destaques,
    })