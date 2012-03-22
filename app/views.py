from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from app.models import Fruit

def home_view(request):
    return render_to_response('home.html', context_instance=RequestContext(request))

@login_required
def account_view(request):
    return render_to_response('account.html', context_instance=RequestContext(request))

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(request.GET.get('next', '/'))
        else:
            return render_to_response('login.html', {'error': True}, context_instance=RequestContext(request))
    return render_to_response('login.html', context_instance=RequestContext(request))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def price_view(request):
    return render_to_response('price.html', {
        'fruits': Fruit.objects.all()
    }, context_instance=RequestContext(request))

def info_view(request):
    return render_to_response('info.html', context_instance=RequestContext(request))

def cart_view(request):
    try:
        request.session['items'].remove(request.GET.get('del'))
        request.session.modified = True
    except:
        pass
    list = []
    for item in request.session.get('items', []):
        list.append(Fruit.objects.get(id=item))
    return render_to_response('cart.html', {
        'fruits': list
    }, context_instance=RequestContext(request))

def buy_view(request, id):
    if request.session.get('items'):
        request.session['items'].add(id)
        request.session.modified = True
    else:
        request.session['items'] = set([id])
    return render_to_response('buy.html', context_instance=RequestContext(request))

def news_view(request):
    return render_to_response('news.html', {
        'fruits': Fruit.objects.all()
    }, context_instance=RequestContext(request))