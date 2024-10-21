from django.views.generic import TemplateView # type: ignore

class HomePageView(TemplateView):
    template_name = "home.html"
