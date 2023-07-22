from django.views.generic import ListView, DetailView

from .models import Material

# Create your views here.


class MaterialListView(ListView):
    model = Material
    paginate_by = 12


class MaterialDetailView(DetailView):
    model = Material
