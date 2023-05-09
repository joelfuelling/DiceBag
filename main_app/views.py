from django.shortcuts import render

die = [ 
  {'sides': '20', 'material': 'Polyurethane', 'color': 'red', 'text_color': 'Black'},
  {'sides': '12', 'material': 'Brass', 'color': 'Brass', 'text_color': 'Brass'},
  {'sides': '10', 'material': 'Polyurethane', 'color': 'black', 'text_color': 'White'},
  {'sides': '8', 'material': 'Wood', 'color': 'Woodgrain', 'text_color': 'Burnt texture'},
  {'sides': '6', 'material': 'Polyurethane', 'color': 'red', 'text_color': 'Black'},
  {'sides': '4', 'material': 'Polyurethane', 'color': 'red', 'text_color': 'Black'},
]
# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def die_index(request):
  return render(request, 'die/index.html', {
    'die': die
  })
                