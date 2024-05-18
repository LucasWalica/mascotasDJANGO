from django.urls import path
from .views import MascotaListView, MascotaDetailView, MascotaCreateView, MascotaDeleteView, TiendaView

urlpatterns = [
    path('', MascotaListView.as_view(), name="mascotas"),
    path('<int:pk>/', MascotaDetailView.as_view(), name="mascota"),
    path('crear/', MascotaCreateView.as_view(), name="crearMascota"),
    path('<int:pk>/delete/', MascotaDeleteView.as_view(), name="borrarMascota"),
    path('tienda/', TiendaView.as_view(), name="tienda")
]

