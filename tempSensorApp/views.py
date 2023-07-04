from django.http import JsonResponse
from .models import TemperatureReading
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# import matplotlib.pyplot as plt
from .utils import get_plot

from django.conf import settings

@csrf_exempt
def data(request):
    if request.method == 'POST':
        temp = request.POST.get('temperature')
        reading = TemperatureReading(temperature=float(temp))
        reading.save()

        # Keep only the most recent 80 readings
        readings_to_keep = 40
        all_readings = TemperatureReading.objects.all().order_by('-time')
        print("Total readings before deletion:", all_readings.count())
        if all_readings.count() > readings_to_keep:
            old_readings = all_readings[readings_to_keep:]
            old_readings.delete()
        print("Total readings after deletion:", TemperatureReading.objects.count())

        return JsonResponse({'status': 'ok'}, status=201)
    else:
        print("Status not ok")
        return JsonResponse({'status': 'not ok'}, status=400)



from django.shortcuts import render

def home(request):
    
    readings = TemperatureReading.objects.all().order_by('-time')
    x=[x.time for x in readings]
    y=[y.temperature for y in readings]
    chart=get_plot(x,y)
    return render(request, 'home.html', {'readings': readings})
    # return render(request, 'home.html', {'chart':chart})

