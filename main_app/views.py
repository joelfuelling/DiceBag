from django.shortcuts import render, redirect
from . models import Die, Condition
from .forms import RollsForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

# def die_index(request):
#   die = Die.objects.all()
#   return render(request, 'die/index.html', {
#     'die': die
#   })

# def die_detail(request, die_id):
#     die = Die.objects.get(id=die_id)
#     return render(request, 'main_app/detail.html', {
#        'die' : die 
#     })

def add_result(request, pk):
    print(request.POST)
    form = RollsForm(request.POST)
    if form.is_valid():
        print("VALID")  
        new_result = form.save(commit=False) #? This one DOES NOT go to the database.
        new_result.die_id = pk
        new_result.save() #? This one goes to the database
    else:
        print(form.errors)    
    return redirect('die_detail', pk=pk)

#new code below here
class DieList(ListView): # our class of DieList is inheriting all of the goodness from that ListView method and...this line of code...#* 'model = Die'
    model = Die

class DieCreate(CreateView):
    model = Die
    fields = '__all__'

class DieUpdate(UpdateView):
    model = Die
    fields = '__all__'

class DieDelete(DeleteView):
    model = Die
    success_url = '/die'

class DieDetail(DetailView):
    model = Die

    def get_context_data(self, **kwargs): # Changed from lesson plan!
        context = super().get_context_data(**kwargs)
        rolls_form = RollsForm()
        context['rolls_form'] = rolls_form
        return context


                