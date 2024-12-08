from django.shortcuts import render, redirect
from .forms import DenunciaForm


def criar_denuncia(request):
    if request.method == "POST":
        form = DenunciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucesso')
    else:
        form = DenunciaForm()
    return render(request, 'denuncia_form.html', {'form': form})


def sucesso(request):
    return render(request, 'sucesso.html')
