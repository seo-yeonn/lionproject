from django.shortcuts import render, get_object_or_404, redirect
from .models import Bloga
from django.utils import timezone
from .forms import CreatePostaForm

# Create your views here.
def home(request):
    blogas = Bloga.objects
    return render(request,'home.html', {'blogas':blogas})

def detail(request, bloga_id):
    bloga_detail = get_object_or_404(Bloga, pk=bloga_id)
    return render(request, 'detail.html', {'bloga_detail':bloga_detail})

def create(request):
    if request.method == 'POST':
        form = CreatePostaForm(request.POST, request.FILES)
        if form.is_valid():
            bloga = form.save(commit=False)
            bloga.pub_date = timezone.datetime.now()
            bloga.save()
        return redirect('/detail/'+str(bloga.id))
    else:
        form = CreatePostaForm()
    return render(request, 'create.html', {'form':form})

def update(request,bloga_id):
    bloga = Bloga.objects.get(id=bloga_id)
    if request.method == 'POST':
        form = CreatePostaForm(request.POST, request.FILES, instance=bloga)
        if form.is_valid():
            bloga = form.save()
            return redirect('/detail/'+str(bloga.id))
    else:
        form = CreatePostaForm(instance=bloga)
        return render(request, 'create.html', {'form':form})

def delete(request, bloga_id):
    bloga = Bloga.objects.get(id=bloga_id)
    bloga.delete()
    return redirect('home')

#     bloga = Bloga()
#     bloga.name = request.GET['name']
#     bloga.age = request.GET['age']
#     bloga.body = request.GET['body']
#     bloga.pub_date = timezone.datetime.now()
#     bloga.save()
#     return redirect('/detail/'+str(bloga.id))
