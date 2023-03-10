# Generated by Django 4.0.3 on 2022-06-15 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_category_remove_article_category_alter_article_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(help_text='Введите название статьи', max_length=100, verbose_name='Название статьи'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(help_text='Введите название рубрики', max_length=50, verbose_name='Название рубрики'),
        ),
        migrations.AlterField(
            model_name='magazine',
            name='title',
            field=models.CharField(help_text='Введите название журнала', max_length=100, verbose_name='Название журнала'),
        ),
    ]
