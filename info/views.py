from django.shortcuts import render


# Create your views here.
def index(request):
    dictionary = ({
        'name': 'Gabriel Antonio Simón Gálvez',
        'github': 'https://github.com/Gaborox/EV1-FrontEnd',
        'personal': ({
            'Correo': 'gabriel.simon@inacapmail.cl',
            'Contacto': '+56988079544',
            'Direccion': 'Coventry 963, Departamento 308, Ñuñoa, RM',
            'Estado civil': 'soltero'
        }),
        'description': 'Soy un estudiante de Ingeniería en Informática, muy comprometido con el desarrollo personal, ' +
                       'amante de los animales y aficionado a los VideoJuegos, tales cómo, Legends of Runaterra.',
        'background': ({
            'Nivel de Estudios Anteriores': 'Enseñanza Media Completa',
            'Estado de Estudios Actuales': 'Estudiante de Ingeniería en Informática INACAP Ñuñoa'
        }),
        'experience': 'Sin experiencia asociada al área.',
        'hobbies': ['Entrenamiento en Gimnasios',
                    'Entretenimiento en base a VideoJuegos',
                    'Paseo de perros en contexto recreativo']
    })

    data = {'data': dictionary}
    return render(request, "info/index.html", data)
