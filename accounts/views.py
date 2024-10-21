from django.urls import reverse_lazy # type: ignore
from django.views.generic import CreateView # type: ignore

from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"