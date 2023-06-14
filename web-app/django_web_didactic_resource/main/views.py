from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def reg(request):
    return render(request, 'main/reg.html')

def generate_tasks(request):
    return render(request, 'main/create_tasks.html')

def generated_tasks(request):
    return render(request, 'main/generated_tasks.html')

def kid_generate_tasks(request):
    return render(request, 'main/create_tasks_kid.html')

def test(request):
    return render(request, 'main/test.html')


def tested_ajax(request):
    # получаем из данных запроса POST отправленные через форму данные
    theme = request.POST.get("choose_theme_dropbox", "Undefined")
    return HttpResponse(f"<h2>В DB было : {theme}</h2>")

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def my_view(request):
    if request.method == "GET":
        data = {'name': request.name, 'phone': 2292747}
        return JsonResponse(data)
    else:
        # Обычный HTTP-запрос
        data = {'name': 'tA', 'phone': 'BLYAT'}
        return HttpResponse('test.html')