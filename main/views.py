from django.shortcuts import render, render_to_response
from main.models import *
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.template import loader
from datetime import *
import random
import string
from django.core.mail import send_mail
from main.forms import ContactForm

SITE_NAME = 'Cool Site' #вынести в настройки
MENU_ITEMS = ({'name': 'Главная', 'link': '/home/', 'pun': ''}, 
              {'name': 'Наши работы', 'link': '/category/', 'pun': ['clips', 'demo', 'concerts'], 'rpun': ['Клипы', 'Промо-ролики', 'Концерты']}, 
              {'name': 'Контакты', 'link': '/contacts/', 'pun': ''})#  ('Главная', 'Категории', 'Контакты')
# Create your views here.
def archive(request):
    inst = Instrument.objects.all()
    return HttpResponse(inst[1])

def home(request):
    category = Category.objects.all()
    context = {
        'sitename': SITE_NAME,
        'categories': category,
        'menu_items': MENU_ITEMS
    }
    return HttpResponse(render_to_string('index.html', context))

def item_s(request):
    try:
        category = Category.objects.all()
    except:
        raise Http404('Ой!!!')
    context = {           #      отправляем в документ html словарь
        'category': category,
        'menu_items': MENU_ITEMS
    }
    return HttpResponse(render_to_string('category.html', context))

def item(request, alias):
    try:
        tovar = Item.objects.get(alias=alias)
    except:
        raise Http404('Ой!!!')
    context = {
        'tovar': tovar
    }
    return HttpResponse(render_to_string('item.html', context))

def get_category(request, alias):
    try:
        category = Category.objects.get(alias=alias)
        tovars = Item.objects.filter(category=category)
    except:
        raise Http404('Ой!!!')
    context = {           #      отправляем в документ html словарь
        'tovars': tovars,
        'category': category,
        'menu_items': MENU_ITEMS
    }
    return HttpResponse(render_to_string('index.html', context))

def search_h(request):
    return HttpResponse(render_to_string('search.html'))

def search(request):
    if 'q' and 't' and 'r' in request.GET:
        message = '1: %r' % request.GET['q'] + '\n' + '2: %r' % request.GET['t'] + '\n' + '3: %r' % request.GET['r'] + '\n' 
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)

@csrf_protect
def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        context = {'form': form,
        'subject': request.POST.get('subject', ''),
        'message': request.POST.get('message', ''),
        }
        if form.is_valid():
            cd = form.cleaned_data
            return HttpResponse(render_to_string('home.html', context))
    else:
        form = ContactForm(initial={'subject': 'I love your'})
        context = {'form': form,
        'subject': request.POST.get('subject', ''),
        'message': request.POST.get('message', ''),
        }
    t = loader.get_template('contact_form.html')
    
    #return render_to_response('contact_form.html', {'form': form})
    request_context = RequestContext(request, context)
    return HttpResponse(t.template.render(request_context))
    # t = loader.get_template('search.html')
    # errors = []
    # context = {
    #         'errors': errors,
    #         'subject': request.POST.get('subject', ''),
    #         'message': request.POST.get('message', ''),
    #     }
    # if request.method == 'POST':
    #     if not request.POST.get('subject', ''):
    #         errors.append('Enter a subject.')
    #     if not request.POST.get('message', ''):
    #         errors.append('Enter a message.')
    #     if not errors:

    # request_context = RequestContext(request, context)
    # return HttpResponse(t.template.render(request_context))