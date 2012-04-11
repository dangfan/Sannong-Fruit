from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from app.models import *

def home_view(request):
    return render_to_response('home.html', context_instance=RequestContext(request))

@login_required
def account_view(request):
    orders = Order.objects.filter(user=request.user)
    return render_to_response('account.html', {
        'orders': orders
    }, context_instance=RequestContext(request))

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
        delid = request.POST.get('del')
        request.session.modified = True
        if delid:
            del request.session['items'][delid]
        list = []
        for item in request.session.get('items', []):
            fruit = Fruit.objects.get(id=item)
            price = fruit.price_list.order_by('-date')[0].price
            amount = request.session['items'][item] = request.POST.get('num' + item, request.session['items'][item])
            orderItem = OrderItem(fruit=fruit, price=price, amount=amount)
            list.append(orderItem)
        if request.method == 'POST' and not delid:
            if not request.user.is_authenticated():
                return HttpResponseRedirect('/login/?next=/cart/')
            order = Order.objects.create(user=request.user)
            for item in list:
                item.order = order
                item.save()
            return HttpResponseRedirect('/account/')
    except:
        pass
    return render_to_response('cart.html', {
        'items': list,
    }, context_instance=RequestContext(request))

def buy_view(request, id):
    if request.session.get('items'):
        request.session['items'][id] = 1
        request.session.modified = True
    else:
        request.session['items'] = {id: 1}
    return render_to_response('buy.html', context_instance=RequestContext(request))

def news_view(request):
    return render_to_response('news.html', {
        'newslist': Post.objects.order_by('-date')
    }, context_instance=RequestContext(request))

def registration_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        phone = request.POST['phone']
        user = User.objects.create_user(username, email, password)
        if user is not None:
            user.first_name = phone
            user.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect(request.GET.get('next', '/'))
        else:
            return render_to_response('registration.html', {'error': True}, context_instance=RequestContext(request))
    return render_to_response('registration.html', context_instance=RequestContext(request))