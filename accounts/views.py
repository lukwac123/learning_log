from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """Rejestracja nowego użytkownika."""
    if request.method != 'POST':
        # Wyświetlanie pustego formularza rejestracji użytkownika.
        form = UserCreationForm()
    else:
        # Przechowywanie wypełnionego formularza.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Zalogowanie nowego użytkownika, a nastęnie przekierowanie go na stronę główną.
            login(request, new_user)
            return redirect('learning_logs:index')
        
    # Wyświetlenie pustego formularza.
    context = {'form': form}
    return render(request, 'registration/register.html', context)

# Create your views here.
