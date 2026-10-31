from django.shortcuts import render

def forum_lista(request):
    return render(request, 'forum/forum_lista.html')

def forum_detalhe(request):
    return render(request, 'forum/forum_detalhe.html')