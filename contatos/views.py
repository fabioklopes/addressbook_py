from os.path import exists

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import random

from contatos.models import Contact, SystemUser


# Create your views here.
def password_generator():
    caracteres = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                  'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
                  'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                  'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'W', 'X', 'Y',
                  'Z', '@', '#', '$', '%', '&', '*']

    senha = ''.join(random.choice(caracteres) for _ in range(8))
    return print(senha)


def contacts(request):
    contact_list = Contact.objects.all()

    # Paginação de resultados na view
    paginator = Paginator(contact_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'contacts.html', {"contact_list": contact_list, "page": page})


def new_contact(request):
    return render(request, 'new_contact.html')


def validate_new_contact(request):
    id = request.POST.get('id')
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    if id and Contact.objects.filter(id=id).exists():
        # Atualiza contato existente
        contato = Contact.objects.get(id=id)
        contato.name = name
        contato.email = email
        contato.phone = phone
        contato.save()
        messages.success(request, 'Contato atualizado com sucesso.')
    else:
        # Cria novo contato
        contato = Contact(
            name=name,
            email=email,
            phone=phone,
            created_by=request.user.username if hasattr(request, 'user') and request.user.is_authenticated else 'anon'
        )
        contato.save()
        messages.success(request, 'Contato adicionado com sucesso.')
    return redirect('contacts')


def security(request):
    return render(request, 'security.html')


def validate_login(request):
    if request.method == 'GET':
        return render(request, 'security.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse('Informações inválidas')


def view_contact(request, id):
    contact = Contact.objects.get(id=id)
    return render(request, 'view_contact.html', {'contact': contact})


def edit_contact(request, id):
    contact = Contact.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        contact.name = name
        contact.email = email
        contact.phone = phone
        contact.save()
        messages.success(request, 'Contato atualizado com sucesso.')
        return redirect('contacts')
    return render(request, 'edit_contact.html', {'contact': contact})


def delete_contact(request, id):
    contact = Contact.objects.get(id=id)
    contact.delete()
    messages.error(request, 'Contato deletado com sucesso.')
    return redirect('/')


def logout_view(request):
    logout(request)
    return redirect('security')


