from django.db import models
from django.core.validators import FileExtensionValidator


class Article(models.Model): #статья
    title = models.CharField(max_length=100, help_text='Введите название статьи', verbose_name='Название статьи', null=False)
    categories = models.ManyToManyField('Category', help_text='Укажите рубрики этого журнала', verbose_name='Рубрики')
    author = models.CharField(max_length=100, help_text='Укажите автора статьи', verbose_name='Автор', null=False)
    date = models.DateField(help_text='Укажите дату создания статьи', verbose_name='Дата', null=False)
    content = models.TextField(help_text='Напишите содержание статьи', verbose_name='Содержание', null=False)
    conclusion = models.TextField(help_text='Напишите вывод статьи', verbose_name='Вывод', null=False)
    image = models.ImageField(upload_to='images_article/', help_text='Загрузите одно изображение', verbose_name='Изображение', null=True)

    # def __str__(self):
    #     return self.title
    def __str__(self):
        # Возвращает строкое представление модели
        if (len(self.title) >= 20):
            return f"{self.title[:20]}..."
        else:
            return self.title


class Category(models.Model): #судя по всему лучше сделать отдельно рубрики
    title = models.CharField(max_length=50, help_text='Введите название рубрики', verbose_name='Название рубрики', null=False)

    def __str__(self):
        return self.title


class Email(models.Model): #эл.почты для рассылки
    email = models.EmailField(help_text='Введите вашу электронную почту', verbose_name='Электронная почта', null=False)

    def __str__(self):
        return self.email


class Magazine(models.Model): #журнал
    title = models.CharField(max_length=100, help_text='Введите название журнала', verbose_name='Название журнала', null=False)
    date = models.DateField(help_text='Укажите дату создания статьи', verbose_name='Дата', null=False)
    # articles = models.ManyToManyField('Article', help_text='Укажите статьи из этого журнала', verbose_name='Статьи', default='1')
    count_article = models.IntegerField(help_text='Укажите количество статей', verbose_name='Количество статей', null=False, default='0')
    count_magazine = models.IntegerField(help_text='Укажите номер журнала', verbose_name='Номер выпуска', null=False, default='0')
    # сделал many to many, чтобы можно было выбирать несколько статей. Если фореджн кеем, то надо будет неудобно указывать журнал при создании статьи
    # Плюсом мало ли они будут одну статью в несколько журналов пихать. Какой нить сборник лучших статей за год или тип того


    image = models.ImageField(upload_to='images_magazine/', help_text='Загрузите одно изображение', verbose_name='Изображение', null=True)
    file = models.FileField(upload_to='files/', help_text='Загрузите PDF журнала', verbose_name='PDF', validators=[FileExtensionValidator(allowed_extensions=['pdf'])], null=True)

    def __str__(self):
        return self.title
