from django.views.generic import TemplateView


class HomepageView(TemplateView):
    """
    View about the homepage of the website
    """

    template_name = "frontend/homepage.html"
