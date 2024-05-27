from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, DeleteView 
from django.urls import reverse_lazy
from .models import Mascota, Items
from .forms import PetCreateForm, EntretenimientoForm, HigieneForm, SaciedadForm, comprarManzanas, comprarJuguetes, comprarJabones

# Create your views here.

class TiendaView(View):
    def get(self, request, *args, **kwargs):
        items = Items.objects.first()
        context = {
            'items':items,
            'compManzanas': comprarManzanas(),
            'compJuguetes': comprarJuguetes(),
            'compJabones':comprarJabones()
        }
        return render(request, 'tienda.html', context)
    
    def post(self, request, *args, **kwargs):
        items = Items.objects.first()
        if 'comprarManzanas' in request.POST:
            items.manzanas += 5
            items.save()
        if 'comprarJabones' in request.POST:
            items.jabones += 5
            items.save()
        if 'comprarJuguetes' in request.POST:
            items.juguetes += 5
            items.save()
        
        items = Items.objects.first()
        context = {
            'items':items,
            'compManzanas': comprarManzanas(),
            'compJuguetes': comprarJuguetes(),
            'compJabones':comprarJabones()
        }
        return render(request, 'tienda.html', context)

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
        items = Items.objects.first()
        context = {
            'mascota':mascota,
            'entretenimiento_form': EntretenimientoForm(),
            'higiene_form':HigieneForm(),
            'saciedad_form':SaciedadForm(),
            'items':items
        }
        return render(request, 'mascotaDetail.html', context)
    
    def post(self, request, pk, *args, **kwargs):
        mascota = get_object_or_404(Mascota, pk=pk)
        items = Items.objects.first()
        
        if 'entretenimiento' in request.POST and items.juguetes > 0:
            mascota.entretenimiento +=1 
            items.juguetes -=1 
            mascota.save()
            items.save()
        elif 'saciedad' in request.POST and items.manzanas > 0:
            mascota.saciedad += 1
            items.manzanas -=1 
            mascota.save()
            items.save()
        elif 'higiene' in request.POST and items.jabones > 0:
            mascota.higiene += 1
            items.jabones -= 1
            mascota.save()
            items.save()
            
        items = Items.objects.first()
        
        context = {
            'mascota': mascota,
            'entretenimiento_form': EntretenimientoForm(),
            'higiene_form': HigieneForm(),
            'saciedad_form': SaciedadForm(),
            'items': items
        }
        return render(request, 'mascotaDetail.html', context) 

class MascotaCreateView( View):
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
            return redirect('mascotas')
        context = {}
        return render(request, 'crear_mascota.html', context)
    
class MascotaDeleteView(DeleteView):
    model = Mascota
    template_name = 'delete_mascota.html'
    success_url = reverse_lazy('mascotas')