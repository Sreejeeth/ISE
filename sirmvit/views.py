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

# def percent(request, category_slug=None):

#         top_labels = ['General Biology', 'Domain', 'Data Analysis', 'Quality Control',
#                       'Critical Research']

#         colors = ['rgba(38, 24, 74, 0.8)', 'rgba(71, 58, 131, 0.8)',
#                   'rgba(122, 120, 168, 0.8)', 'rgba(164, 163, 204, 0.85)',
#                   'rgba(190, 192, 213, 1)']
        
#         category = None
#         categories = Category.objects.all()
#         products = Studentdbs.objects.filter(available=True)

#         # for c in categories:
#         #      if category.slug == c.slug:
#         if category_slug:
#             category = get_object_or_404(Category, slug=category_slug)
#             products = products.filter(category=category)
#             print("Hello")
        
#         x_data=[]
#         y_data=[]


#         for product in products:
#             lst=[round(((product.general_biology)/38)*100,2),round(((product.domain)/38)*100,2),round(((product.data_analysis)/38)*100,2),round(((product.quality_control)/38)*100,2),round(((product.critical_research)/38)*100,2)]    
#             x_data.append(lst)
#             y_data.append(product.name+'\n'+product.email_address+'\n'+product.contact_no)
      


#         traces = []

#         for i in range(0, len(x_data[0])):
#             for xd, yd in zip(x_data, y_data):
#                 traces.append(go.Bar(
#                     x=[xd[i]],
#                     y=[yd],
#                     orientation='h',
#                     marker=dict(
#                         color=colors[i],
#                         line=dict(
#                                 color='rgb(248, 248, 249)',
#                                 width=1)
#                     )
#                 ))

#         layout = go.Layout(
#             xaxis=dict(
#                 showgrid=False,
#                 showline=False,
#                 showticklabels=False,
#                 zeroline=False,
#                 domain=[0.15, 1]
#             ),
#             yaxis=dict(
#                 showgrid=False,
#                 showline=False,
#                 showticklabels=False,
#                 zeroline=False,
#             ),
#             barmode='stack',
#             paper_bgcolor='rgb(248, 248, 255)',
#             plot_bgcolor='rgb(248, 248, 255)',
#             margin=dict(
#                 l=120,
#                 r=10,
#                 t=140,
#                 b=80
#             ),
#             showlegend=False,
#         )

#         annotations = []

#         for yd, xd in zip(y_data, x_data):
#             # labeling the y-axis
#             annotations.append(dict(xref='paper', yref='y',
#                                     x=0.14, y=yd,
#                                     xanchor='right',
#                                     text=str(yd),
#                                     font=dict(family='Arial', size=14,
#                                               color='rgb(67, 67, 67)'),
#                                     showarrow=False, align='right'))
#             # labeling the first percentage of each bar (x_axis)
#             annotations.append(dict(xref='x', yref='y',
#                                     x=xd[0] / 2, y=yd,
#                                     text=str(xd[0]) + '%',
#                                     font=dict(family='Arial', size=14,
#                                               color='rgb(248, 248, 255)'),
#                                     showarrow=False))
#             # labeling the first Likert scale (on the top)
#             if yd == y_data[-1]:
#                 annotations.append(dict(xref='x', yref='paper',
#                                         x=xd[0] / 2, y=1.1,
#                                         text=top_labels[0],
#                                         font=dict(family='Arial', size=14,
#                                                   color='rgb(67, 67, 67)'),
#                                         showarrow=False))
#             space = xd[0]
#             for i in range(1, len(xd)):
#                     # labeling the rest of percentages for each bar (x_axis)
#                     annotations.append(dict(xref='x', yref='y',
#                                             x=space + (xd[i]/2), y=yd, 
#                                             text=str(xd[i]) + '%',
#                                             font=dict(family='Arial', size=14,
#                                                       color='rgb(248, 248, 255)'),
#                                             showarrow=False))
#                     # labeling the Likert scale
#                     if yd == y_data[-1]:
#                         annotations.append(dict(xref='x', yref='paper',
#                                                 x=space + (xd[i]/2), y=1.1,
#                                                 text=top_labels[i],
#                                                 font=dict(family='Arial', size=14,
#                                                           color='rgb(67, 67, 67)'),
#                                                 showarrow=False))
#                     space += xd[i]

#         layout['annotations'] = annotations

#         fig = go.Figure(data=traces, layout=layout)
#         py.plot(fig, filename='bar-colorscale')


#         return render(request, 'home.html', {'category': category,
#                                                       'categories': categories,
#                                                       'products': products})       

def search(request):
    if request.method=='POST':
        srch = request.POST['srh']

        if srch:
            match= Studentdbs.objects.filter(Q(contact_no__icontains=srch) |
                                            Q(name__icontains=srch))
            if match:
                 return render(request,'search.html', { 'sr' :match})
            else :
                messages.error(request,' no result found')
        else:
            return HttpResponseRedirect('/search/')
    return render(request,'search.html')
