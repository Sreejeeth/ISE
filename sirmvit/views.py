from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from sirmvit.models import Studentdbs,Category
from django.shortcuts import render, get_object_or_404

from django.db.models import Q
from django.contrib import messages

@login_required
def home(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Studentdbs.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'home.html', {'category': category,
                                                          'categories': categories,
                                                          'products': products})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Studentdbs.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'list.html', {'category': category,
                                                      'categories': categories,
                                                      'products': products})



# def about(request):
#     about_list = About.objects.all()
#     about_dict = {"about_records":about_list}
#     return render(request,'about.html',about_dict)
#
# def checkout(request):
#         return render(request,'checkout.html')

def front(request):
        return render(request,'front.html')

def search(request):
    if request.method=='POST':
        srch = request.POST['srh']

        if srch:
            match= Studentdbs.objects.filter(Q(USN__icontains=srch) |
                                            Q(name__icontains=srch))
            if match:
                 return render(request,'search.html', { 'sr' :match})
            else :
                messages.error(request,' no result found')
        else:
            return HttpResponseRedirect('/search/')
    return render(request,'search.html')
