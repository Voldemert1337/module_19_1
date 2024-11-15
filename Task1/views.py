from django.shortcuts import render
from .forms import UserRegistrationForm
from django.http import HttpResponse
from .models import Buyer, Game
from django.core.paginator import Paginator
# Create your views here.


def home(request):
    return render(request, 'first_task1/home.html')


def about(request):
    return render(request, 'first_task1/about.html')


def products(request):
    return render(request, 'first_task1/products.html')


def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            age = int(form.cleaned_data['age'])
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']

            print(f"Username: {username}, Age: {age}, Password: {password}, Repeat Password: {repeat_password}")

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                print('Пароли не совпадают')
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
                print('Возраст меньше 18')
            elif Buyer.objects.filter(name=username).exists():
                info['error'] = 'Пользователь уже существует'
                print('Пользователь уже существует')
            else:
                Buyer.objects.create(name=username, age=age, balance=0.00)
                return HttpResponse(f"Приветствуем, {username}!")
        else:
            info['form'] = form
            print('Форма некорректно заполнена')
    else:
        form = UserRegistrationForm()
        info['form'] = form

    return render(request, 'first_task1/registration_page.html', info)


def product_list(request):
    game_list = Game.objects.all()
    per_page = request.GET.get('per_page', 10)  # Получение количества элементов на странице из запроса
    paginator = Paginator(game_list, per_page)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj, 'per_page': per_page}
    return render(request, 'first_task1/products.html', context)

