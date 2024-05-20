from mascota.models import Mascota
from background_task import background

@background(schedule=60)
def my_task():    
    mascotas = Mascota.objects.all()
    for mascota in mascotas:
        mascota.entretenimiento = max(mascota.entretenimiento - 1, 0)
        mascota.saciedad = max(mascota.saciedad - 1, 0)
        mascota.higiene = max(mascota.higiene - 1, 0)

        mascota_mal_count = 0
        if mascota.entretenimiento <= 3:
            mascota_mal_count += 1
        if mascota.saciedad <= 3:
            mascota_mal_count += 1
        if mascota.higiene <= 3:
            mascota_mal_count += 1
        mascota.hp = max(mascota.hp - mascota_mal_count, 0)
        mascota.save()
        

my_task(repeat=7200)