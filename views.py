from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, DeleteView 
from django.urls import reverse_lazy
from .models import Mascota
from .forms import PetCreateForm

# Create your views here.

class MascotaListView(View):
    def get(self, request, *args, **kwargs):
        mascotas = Mascota.objects.all()
        context = {
            'mascotas':mascotas
        }
        return render(request, 'listaMascotas.html', context)

class MascotaDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        mascota = get_object_or_404(Mascota, pk = pk )
        context = {
            'mascota':mascota
        }
        return render(request, 'mascotaDetail.html', context)

class MascotaCreateView(View):
    def get(self, request, *args, **kwargs):
        form = PetCreateForm()
        context = {
            'form':form
        }
        return render(request, 'crear_mascota.html',context)
    def post(self, request, *args, **kwargs):
        form = PetCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        context = {}
        return render(request, 'crear_mascota.html', context)
    
class MascotaDeleteView(DeleteView):
    model = Mascota
    template_name = 'delete_mascota.html'
    success_url = reverse_lazy('home')