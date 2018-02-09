from django.db import models
from datetime import *

class TipInstr(models.Model):
	name = models.CharField(max_length=55, verbose_name='Название')

	class Meta:
		verbose_name = 'типа'
		verbose_name_plural = 'типов'

	def __str__(self):
		return 'Инструмент %s' % self.name

class Instrument(models.Model):
	name = models.CharField(max_length=55, verbose_name='Название')
	tip = models.ForeignKey(TipInstr, blank=True, null=True)

	class Meta:
		verbose_name = 'Инструмент'
		verbose_name_plural = 'Инструменты'

	def __str__(self):
		return '%s' % self.name

class Musicant(models.Model):
	name = models.CharField(max_length=55, verbose_name='Имя')
	ser_name = models.CharField(max_length=55, verbose_name='Фамилия')
	age = models.SlugField()#(default=date.today, verbose_name='Дата рождения')
	instrument = models.ForeignKey(Instrument, blank=True, null=True)
	style = models.CharField(max_length=55, verbose_name='Стиль')
	level = models.CharField(max_length=2, verbose_name='Уровень игры')

	class Meta:
		verbose_name = 'Музыкант'
		verbose_name_plural = 'Музыканты'

	def __str__(self):
		return 'Musicman %s' % self.instrument




class Category(models.Model):
	name = models.CharField(max_length=255, verbose_name='Название категории')
	alias = models.SlugField(verbose_name='Alias категории')

	class Meta:
		verbose_name = 'Категория видео'
		verbose_name_plural = 'Категории видео'

	def __str__(self):
		return 'Категория %s' % self.name

class Tipa(models.Model):
	name = models.CharField(max_length=255, verbose_name='Катекория новости')
	alias = models.SlugField(verbose_name='Alias tipa')

	class Meta:
		verbose_name = 'Категория новости'
		verbose_name_plural = 'Категории новостей'
		
	def __str__(self):
		return 'Тип %s' % self.name

class News(models.Model):
	name = models.CharField(max_length=255, verbose_name='Название')
	text = models.CharField(max_length=255, verbose_name='Текст')
	alias = models.SlugField(verbose_name='Alias')
	tipa = models.ForeignKey(Tipa)

	class Meta:
		verbose_name = 'Новость'
		verbose_name_plural = 'Новости'

	def __str__(self):
		return 'Новость %s' % self.name		

class Video(models.Model):
	name = models.CharField(max_length=255, verbose_name='Название')
	text = models.CharField(max_length=255, verbose_name='Описание')
	link = models.CharField(max_length=255, verbose_name='Link to video')

	category = models.ForeignKey(Category) #ссылка на класс

	class Meta:
		verbose_name = 'Видео'
		verbose_name_plural = 'Видео'

	def __str__(self):
		return 'video %s' % self.name