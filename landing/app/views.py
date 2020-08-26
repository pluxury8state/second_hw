from collections import Counter

from django.shortcuts import render

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
from django.http import HttpResponse
from django.urls import reverse

counter_show = Counter()
counter_click = Counter()





def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    pages = {
        '1-ая страница лендинга': reverse('index'),
    }
    context = {
        'pages': pages
    }

    if request.GET.get('from-landing') == 'original':
        counter_click['val_original'] += 1
        template_name = 'landing_alternate.html'

        return render(request, template_name, context)

    elif request.GET.get('from-landing') == 'test':
        counter_click['val_test'] += 1
        template_name = 'landing.html'

        return render(request, template_name, context)

    else:
        return HttpResponse('перехода с лэндинга не произошло')



def landing(request):

    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов


    if request.GET.get('ab-test-arg') == 'original':
        counter_show['show_original'] += 1
        template_name = 'landing.html'
        return render(request, template_name)

    elif request.GET.get('ab-test-arg') == 'test':
        counter_show['show_test'] += 1
        template_name = 'landing_alternate.html'
        return render(request, template_name)

    else:
        return HttpResponse('не указано нужное значение в опциональном параметре ab-test-arg или этот параметр не указан вообще')


def stats(request):


    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Для вывода результат передайте в следующем формате:
    # return render_to_response('stats.html', context={
    #     'test_conversion': 0.5,
    #     'original_conversion': 0.4,
    # })
    try:
       context = {
           'original_conversion': float(counter_click['val_original']/counter_show['show_original']),
           'test_conversion': float(counter_click['val_test']/counter_show['show_test'])
       }
    except ZeroDivisionError as E:
        return HttpResponse(str(E))
    else:

        template_name = 'stats.html'
        return render(request, template_name, context)