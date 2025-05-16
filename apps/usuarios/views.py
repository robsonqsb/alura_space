from django.shortcuts import redirect, render
from apps.usuarios.forms import CadastroForms, LoginForms
from django.contrib.auth.models import User
from django.contrib import auth, messages

def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            login = form['nome_login'].value()
            senha = form['senha'].value()        

        usuario = auth.authenticate(
            request,
            username = login,
            password = senha
        )

        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, f'Usuário {login} logado com sucesso!')
            return redirect('index')
        else:
            messages.error(request, 'Erro ao efetuar login!')
            return redirect('login')

    return render(request, 'usuarios/login.html', {"form": form})    

def cadastro(request):
    form = CadastroForms()
    if request.method == 'POST':
        form = CadastroForms(request.POST)
        
        if form.is_valid():
            nome = form['nome_cadastro'].value()
            email = form['email'].value()
            senha = form['senha1'].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request, 'Nome de usuário já existe!')
                return redirect('cadastro')
            
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )

            usuario.save()
            messages.success(request, 'Usuário incluído com sucesso!')
            return redirect('login')
        
    return render(request, 'usuarios/cadastro.html', {"form": form})

def logout(request):
    messages.success(request, 'Usuário desconectado!')
    auth.logout(request)
    return redirect('login')
