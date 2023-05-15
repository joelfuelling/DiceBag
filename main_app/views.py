from django.shortcuts import render, redirect
from .models import Die, Condition
from .forms import RollsForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def add_result(request, pk):

    form = RollsForm(request.POST)
    if form.is_valid():
        new_result = form.save(commit=False) #? This one DOES NOT go to the database.
        new_result.die_id = pk
        new_result.save() #? This one goes to the database
        return redirect('die_detail', pk=pk)
    else:  
      return redirect('die_detail', pk=pk)  
    

#*views.assoc_condition view function
def assoc_condition(request, die_id, condition_id):
   # Note that you can pass a conditions's id instead of the whole condition object
   Die.objects.get(id=die_id).condition.add(condition_id)
   return redirect('die_detail', pk=die_id)

def remove_condition(request, die_id, condition_id):
   # Note that you can pass a conditions's id instead of the whole condition object
   Die.objects.get(id=die_id).condition.remove(condition_id)
   return redirect('die_detail', pk=die_id)


class DieList(ListView): # our class of DieList is inheriting all of the goodness from that ListView method and...this line of code...#* 'model = Die'
    model = Die

class DieCreate(CreateView):
    model = Die
    fields = ['sides', 'material', 'color', 'text_color']
    #? orinially this started as 'fields = "__all__"'. However, after we added 'conditions, it showed up on the create field and caused an error. You could also try to use excludes here.

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
        die = self.get_object()
        id_list = die.condition.all().values_list('id', flat=True)
        conditions_die_doesnt_have = Condition.objects.exclude(id__in=id_list)
        context['conditions_die_doesnt_have'] = conditions_die_doesnt_have
        context['rolls_form'] = rolls_form
        return context
    
    # ! Below is the function defined version of the CLASS BASED function we used above instead.
    # def die_detail(request, die_id):
    #   #? is die_detail OK with die below? It was Cats and cat in the walkthrough.
    #   die = Die.objects.get(id=die_id)
    #   # Get the condition the  doesn't have...
    #   # First, create a list of the toy ids that the die DOES have
    #   id_list = die.condition.all().values_list('id')
    #   # Now we can query for condition whose ids are not in the list using exclude
    #   condition_die_doesnt_have = Condition.objects.exclude(id__in=id_list)
    #   rolls_form = RollsForm()
    #   return render(request, 'die/detail.html', {
    #   'die': die, 'rolls_form': rolls_form,
    #   # Add the condition to be displayed
    #   'condition': condition_die_doesnt_have
  # })
    
class ConditionList(ListView):
  model = Condition

class ConditionDetail(DetailView):
  model = Condition

class ConditionCreate(CreateView):
  model = Condition
  fields = '__all__'

class ConditionUpdate(UpdateView):
  model = Condition
  fields = ['name', 'condition']

class ConditionDelete(DeleteView):
  model = Condition
  success_url = '/conditions_die_doesnt_have'


                