from django.shortcuts import render
from django.http import HttpResponse
import math

# Create your views here.
def index(request):
    context = {
        'titulo': "Formulario",
    
    }
    return render(request, 'encuesta/formulario.html', context)

def enviar (request): 
    context= {
        'titulo': "Respuesta",
        'nombre' : request. POST['nombre'],
        'clave': request. POST['password'], 
        'educacion': request. POST['educacion'], 
        'nacionalidad': request. POST['nacionalidad'], 
        'idiomas': request.POST.getlist('idiomas'),
        'correo': request.POST['email'],
        'website': request. POST['sitioweb'],
    }
    return render (request, 'encuesta/respuesta.html', context)

# ACTIVIDAD 3: MOSTRAR FORMULARIO DE CALCULADORA
def calculadora(request):
    contexto = {
        'title': 'Calculadora',
    }
    return render(
        request,
        'encuesta/calculadora.html',
        contexto
    )


# ACTIVIDAD 3: PROCESAR OPERACION MATEMATICA
def resultado_calculadora(request):
    if request.method != 'POST':
        return HttpResponse(
            'Debes enviar los datos desde el formulario.',
            status=405
        )

    try:
        numero1 = float(request.POST.get('numero1', ''))
        numero2 = float(request.POST.get('numero2', ''))
        operacion = request.POST.get('operacion', '')

        if operacion == 'suma':
            resultado = numero1 + numero2
            simbolo = '+'
            nombre_operacion = 'suma'

        elif operacion == 'resta':
            resultado = numero1 - numero2
            simbolo = '-'
            nombre_operacion = 'resta'

        elif operacion == 'multiplicacion':
            resultado = numero1 * numero2
            simbolo = '*'
            nombre_operacion = 'multiplicacion'

        else:
            return HttpResponse(
                'La operacion seleccionada no es valida.',
                status=400
            )

        contexto = {
            'numero1': numero1,
            'numero2': numero2,
            'resultado': resultado,
            'simbolo': simbolo,
            'nombre_operacion': nombre_operacion,
        }

        return render(
            request,
            'encuesta/resultado_calculadora.html',
            contexto
        )

    except (ValueError, TypeError):
        return HttpResponse(
            'Ingresa dos numeros validos.',
            status=400
        )
# ACTIVIDAD 3: MOSTRAR FORMULARIO DE Cilindro
def cilindro(request):
    contexto = {
        'title': 'Cilindro',
    }
    return render(
        request,
        'encuesta/cilindro.html',
        contexto
    )
           
# ACTIVIDAD 3: calcular volumen del cilindro
def resultado_cilindro(request):
    if request.method != 'POST':
        return HttpResponse(
            'Debes enviar los datos desde el formulario.',
            status=405
        )

    try:
        altura = float(request.POST.get('altura', 0))
        diametro = float(request.POST.get('diametro', 0))

        if altura <= 0 or diametro <= 0 :
            return HttpResponse(
                'La altura y diametro deben ser mayores que 0.',
                status=400
            )

        radio = diametro/2
        volumen = math.pi* radio** 2 * altura

        contexto = {
            'altura': altura,
            'diametro': diametro,
            'radio': radio,
            'volumen': volumen,
            
        }

        return render(
            request,
            'encuesta/resultado_cilindro.html',
            contexto
        )

    except (ValueError, TypeError):
        return HttpResponse(
            'Ingrese una altura y diametro validos.',
            status=400
        )