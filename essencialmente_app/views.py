from django.shortcuts import render

from django.contrib import messages

from .forms import Avaliar_IMCModelForm

def index(request): #vai fazer uma requisição ao servidor
    return render(request,'index.html')#trazendo a pagina ao html
def avaliacao(request):
    if request.method == 'POST':
        form = Avaliar_IMCModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #chamar o formulario de novo para limpar 
            messages.success(request,'dados salvos com sucesso')
        else:
            messages.error(request,'Erro ao salvar os dados')
    else:
        form = Avaliar_IMCModelForm()
    context = {
        'form':form
    }

    return render(request,'avaliacao.html',context)