# expense_tracker/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BootstrapAuthenticationForm, ExpenseForm

def login_view(request):
    if request.method == 'POST':
        form = BootstrapAuthenticationForm(request, request.POST)
        if form.is_valid():
            # Autenticação bem-sucedida, redirecionar para a página de dashboard
            return redirect('dashboard')
    else:
        form = BootstrapAuthenticationForm(request)
    return render(request, 'login.html', {'form': form})

@login_required
def dashboard(request):
    # Lógica para carregar dados do dashboard
    return render(request, 'dashboard.html')

@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            # Despesa adicionada com sucesso, redirecionar para a página de dashboard ou outra página
            return redirect('dashboard')
    else:
        form = ExpenseForm()
    return render(request, 'add_expense.html', {'form': form})
