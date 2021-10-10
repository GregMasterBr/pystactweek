from django.http.response import Http404
from django.shortcuts import render,redirect
from django.http import HttpResponse
import hashlib
from .models import Usuario
# Create your views here.

def cadastro(request):
    if request.session.get('usuario'):
        return redirect('/home/')    
    #return HttpResponse('Estou na página de cadastro')
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status': status})


def login(request):
    if request.session.get('usuario'):
        return redirect('/home/')    
    status = request.GET.get('status')
    #return HttpResponse('Estou na página de login')    
    return render(request, 'login.html' ,{'status': status})

def valida_cadastro(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    usuario_existe = Usuario.objects.filter(email = email)

    if len(usuario_existe) > 0:
        return redirect('/auth/cadastro/?status=1')
    
    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        return redirect('/auth/cadastro/?status=2')
    
    if len(senha) < 8 or len(senha) > 12:
        return redirect('/auth/cadastro/?status=3')

    try:
        senha = hashlib.sha256(senha.encode()).hexdigest()
        usuario = Usuario(nome=nome,
                            senha=senha,
                            email=email)
        usuario.save()
        return redirect('/auth/cadastro/?status=0')
    except:
        return redirect('/auth/cadastro/?status=4')                              

    #return HttpResponse(f'Estou na página de validacao de cadastro do {nome} {email} com a senha {senha}')    
      
def valida_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha = hashlib.sha256(senha.encode()).hexdigest()
    usuarios = Usuario.objects.filter(email = email).filter(senha = senha)

    if len(usuarios) == 0:
        return redirect('/auth/login/?status=1')
    elif len(usuarios) > 0:
        request.session['usuario'] = usuarios[0].id
        #return HttpResponse('Logado')
        return redirect('/home/')

def sair(request):
    request.session.flush()
    return redirect('/auth/login/')        