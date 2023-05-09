from django.shortcuts import render

from . models import Die
# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def die_index(request):
  die = Die.objects.all()
  return render(request, 'die/index.html', {
    'die': die
  })

def die_detail(request, die_id):
    die = Die.objects.get(id=die_id)
    return render(request, 'die/detail.html', {
       'die' : die 
    })
                