from django.shortcuts import render, redirect
from .forms import EmailForm

from django.http import HttpResponse, HttpResponseRedirect

from .models import Article, Magazine, Email, Category
from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from django.conf import settings
from django.core.mail import send_mail, send_mass_mail
import os
import random
import datetime

'''
@receiver(post_save, sender=Article)  # админ добавил новую статью
def new_article(sender, instance, created, **kwargs):
    if created:
        try:
            message = []
            emails = Email.objects.all()

            theme = 'На сайте Lean Green Smart новая статья!'
            content = f'Здравствуйте! На нашем сайте вышла новая статья. Вы можете ознакомиться с ней по следующей ссылке: 127.0.0.1:8000/articles/{instance.pk}'
            # потом ссылку поменять надо будет, пока лень с этим танцевать
            for email in emails:
                s = (theme, content, settings.EMAIL_HOST_USER, [email.email])
                message.append(s)

            send_mass_mail(message, fail_silently=False)

            print(f'Рассылка писем прошла успешно!')

        except:
            print('При рассылке писем произошла ошибка! Скорее всего есть нерабочие почты.')
        # если не лень, то нормально обработать исключения


@receiver(pre_save, sender=Article) # админ изменил статью
def update_article(sender, instance, **kwargs):
    try:
        old_arcticle = Article.objects.get(id = instance.id)
        if not old_arcticle.image == instance.image:
            try:
                os.remove(r"./media/" + str(old_arcticle.image))
                print("Старая картинка статьи удалена.")
            except:
                print("Не удалось удалить старую картинку статьи")
        print("Админ изменил статью")

    except:
        print("Админ добавил новую статью")
        # да, можно сюда перенести функцию new_article, но тогда я не могу получить данные новой статьи
        # пишет instance.id = None

@receiver(post_delete, sender=Article) # админ удалил статью
def delete_article(sender, instance, **kwargs):
    try:
        os.remove(r"./media/"+str(instance.image))
        print("Админ удалил статью")
    except:
        print("Админ удалил статью, но не удалось удалить картинку")


@receiver(post_save, sender=Magazine) # админ добавил новый журнал
def new_magazine(sender, instance, created, **kwargs):
    if created:
        try:
            message = []
            emails = Email.objects.all()

            theme = 'На сайте Lean Green Smart новый выпуск журнала!'
            content = f'Здравствуйте! На нашем сайте вышел новый выпуск журнала. Вы можете ознакомиться с ним по следующей ссылке: 127.0.0.1:8000/magazines/{instance.pk}'
            # потом ссылку поменять надо будет, пока лень с этим танцевать
            for email in emails:
                s = (theme, content, settings.EMAIL_HOST_USER, [email.email])
                message.append(s)

            send_mass_mail(message, fail_silently=False)

            print(f'Рассылка писем прошла успешно!')

        except:
            print('При рассылке писем произошла ошибка! Скорее всего есть нерабочие почты.')
        # если не лень, то нормально обработать исключения


@receiver(pre_save, sender=Magazine) # админ изменил журнал
def update_magazine(sender, instance, **kwargs):

    try: #изменил журнал
        old_magazine = Magazine.objects.get(id = instance.id)
        if not old_magazine.image == instance.image:
            try:
                os.remove(r"./media/" + str(old_magazine.image))
                print("Старая картинка журнала удалена")
            except:
                print("Не удалось удалить старую картинку журнала")
        if not old_magazine.file == instance.file:
            try:
                os.remove(r"./media/" + str(old_magazine.file))
                print("Старый файл журнала удален")
            except:
                print("Не удалось удалить старый файл журнала")
        print("Админ изменил журнал")

    except:
        print("Админ добавил новый журнал")


@receiver(post_delete, sender=Magazine) # админ удалил журнал
def delete_magazine(sender, instance, **kwargs):
    try:
        os.remove(r"./media/"+str(instance.image))
    except:
        print("Не удалось удалить картинку")
    try:
        os.remove(r"./media/" + str(instance.file))
    except:
        print("Не удалось удалить файл")
    print("Админ удалил журнал")
'''

# Главная страница ---------------------------------------------------------------------------------------
def index(request):
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('home')
            
    form = EmailForm()
    magazines = Magazine.objects.order_by('-date')[:3]
    
    context = {
        'magazines': magazines,
        'form':form
    }
    return render(request, 'mainapp/index.html', context)

def about(request):
    return render(request, 'mainapp/about.html')

# def email_new(request):
#     return render(request)

# Страница со статьями ---------------------------------------------------------------------------------------
def articles(request):
    selected_filter = request.GET.get('filter')
    #print(selected_filter)

    if selected_filter == None:
        #return HttpResponseRedirect('articles?filter=new')
        selected_filter = "new"

    if selected_filter == "new":  # от новых к старым
        articles = Article.objects.all().order_by('-date')

    else:  # от старых к новым
        articles = Article.objects.all().order_by('date')

    return render(request, 'mainapp/articles.html', {'articles':articles, 'selected_filter':selected_filter})

# Страница со статьей-------------------------------------------------------------------------------------
def article(request, id):
    article = Article.objects.get(id=id)
    mag = Magazine.objects.filter(articles=article) # получаем список журналов, в которых есть эта статья (в идеале такой журнал 1)
                                                    # если журналов несколько, то получается берем самый последний (самый свежий)
    magazine = mag.last()

    # ещё из рубрики. Если у нашей статьи несколько рубрик, берем просто первую
    cat = article.categories.all().first()


    articles_db = Article.objects.filter(categories=cat) # получаем все статьи из этой рубрики
    articles = [] # список нужен затем, потому что выше мы получаем querrySet и его нужно перебрать


    # Рандомный вывод статей в предложке----------------------------------------------------------------------------------
    '''
    r = [] # тут я по тупому делаю рандомные статьи
    i = 0

    for _ in articles_db:
        r.append(i)
        i += 1

    random.shuffle(r) # получается список рандомных индексов
    #print(r)

    k = 0
    for art in r:
        if k < 5:
            if articles_db[art] != article: # если нам попалась статья, которая сейчас открыта, то скипаем
                articles.append(articles_db[art]) # и получается беру первые 5 рандомных статей
            else:
                k -= 0
        k += 1
    '''

    return render(request, 'mainapp/article.html', {'article':article, 'magazine':magazine, 'articles':articles, 'category':cat})


def archive(request):
    magazines = Magazine.objects.all()
    dates = Magazine.objects.all().values_list('date')
    new_date = []
    for date in dates:
        if date[0].year not in new_date:
            new_date.append(date[0].year)
        new_date.sort(reverse=True)
    return render(request, 'mainapp/archive.html', {'magazines':magazines, 'dates': new_date})


def for_authors(request):
    return render(request, 'mainapp/for_authors.html')

def send_article(request):
    return render(request, 'mainapp/send_article.html')



# Поиск по статьям---------------------------------------------------------------------------------------------
'''
def search(request): # без html пока лень с этим возиться. Боюсь подводных камней при передаче и показе в html
    # такой поиск у меня на своём сайте, заведомо рабочее
    ser = request.GET.get('search_str')
    ser = ser.strip()
    ser = ser.title()
    articles = Article.objects.all()
    result = []

    for article in articles:
        if ser in article.title.title(): # сначала ищем по названию
            if article not in result:
                result.append(article)

    for article in articles:
        for category in article.categories.all(): # по рубрике
            if ser in category.title.title():
                if article not in result:
                    result.append(article)

    for article in articles:
        if ser in article.author.title():  # по автору
            if article not in result:
                result.append(article)

    for article in articles:
        if ser in article.content.title():  # по содержанию
            if article not in result:
                result.append(article)

    for article in articles:
        if ser in article.conclusion.title():  # по выводу
            if article not in result:
                result.append(article)

    return HttpResponseRedirect('/') # пока возвращаемся сюда, как бы заглушка
'''
