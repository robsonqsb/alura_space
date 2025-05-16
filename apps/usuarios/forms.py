from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label="Login",
        required=True,
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Infome o login"}),
    )
    senha = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Informe a senha"}),
    )

class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label="Nome",
        required=True,
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Infome o nome"}),
    )
    email = forms.EmailField(
        label="E-mail",
        required=True,
        max_length=100,
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Infome o e-mail"}),
    )
    senha1 = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Informe a senha"}),
    )
    senha2 = forms.CharField(
        label="Confirmação Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Informe a senha de confirmação"}),
    )

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get("nome_cadastro")

        if nome:
            nome = nome.strip()            
            if " " in nome:                
                raise forms.ValidationError("Não é possível inserir espaços nesse campo")
            else:
                return nome
            
    def clean_senha2(self):
         senha_1 = self.cleaned_data.get("senha1")
         senha_2 = self.cleaned_data.get("senha2")

         if senha_1 and senha_2:
              if senha_1 != senha_2:
                   raise forms.ValidationError("As senhas não são iguais!")
              else:
                   return senha_2
               
              
         
