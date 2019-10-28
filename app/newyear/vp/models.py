from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Main(models.Model):
	main = models.ImageField('Шапка', upload_to='main', blank=True)
	logo = models.ImageField('Логотип', upload_to='main', blank=True)
	bg = models.ImageField('Фон', upload_to='main', blank=True)
	icon = models.ImageField('Иконка', upload_to='main', blank=True)

	def __str__(self):
		return "%s | %s | %s | %s" % (self.main, self.logo, self.bg, self.icon)

	class Meta:
		verbose_name = 'Шапка, логотип, фон, иконка сайта'
		verbose_name_plural = 'Шапка, логотип, фон, иконка сайта'

class TopNumbersLeft(models.Model):
	city = models.CharField('Город', max_length=250, default='', db_index=True)
	phone = models.CharField('Номер телефона', max_length=20, default='', db_index=True)

	def __str__(self):
		return '{}'.format(self.city)

	class Meta:
		verbose_name = 'Номера телефонов слева в шапке сайта'
		verbose_name_plural = 'Номера телефонов слева в шапке сайта'

class TopNumbersRight(models.Model):
	city = models.CharField('Город', max_length=250, default='', db_index=True)
	phone = models.CharField('Номер телефона', max_length=20, default='', db_index=True)

	def __str__(self):
		return '{}'.format(self.city)

	class Meta:
		verbose_name = 'Номера телефонов справа в шапке сайта'
		verbose_name_plural = 'Номера телефонов справа в шапке сайта'

class Title(models.Model):
	title = models.CharField('Название страницы сайта', max_length=250, default='', db_index=True)
	name_page = models.CharField('Краткое описание страницы сайта', max_length=250, default='Сладкие Новогодние подарки для детей 2020', db_index=True, blank=True)
	h1 = models.CharField('Заголовок h1 страницы сайта', max_length=250, default='', db_index=True, blank=True)
	description = models.TextField('Краткое описание сайта', default='', blank=True)
	h2 = models.CharField('Заголовок h2 страницы сайта', max_length=250, default='', blank=True)
	description2 = models.TextField('Краткое описание сайта 2', default='', blank=True)
	h3_classic = models.CharField('Заголовок h3 для классики', max_length=250, default='', blank=True)
	descript_classic = models.TextField('Краткое описание для классики', default='', blank=True)
	h3_premium = models.CharField('Заголовок h3 для премиум', max_length=250, default='', blank=True)
	descript_premium = models.TextField('Краткое описание для премиум', default='', blank=True)

	def __str__(self):
		return "%s | %s" % (self.id, self.title)

	class Meta:
		verbose_name = 'ID | Страницы сайта'
		verbose_name_plural = 'Страницы сайта'

class Images(models.Model):
	images = models.ImageField('Изображения сайта', upload_to='', blank=True)

	def __str__(self):
		return '{}'.format(self.images)

	class Meta:
		verbose_name = 'Изображения сайта'
		verbose_name_plural = 'Изображения сайта'

class Classic(models.Model):
	title = models.CharField('Название', max_length=250, db_index=True)
	series = models.CharField('Серия', max_length=50, default='Классика', db_index=True)
	media = models.CharField('Изображение', max_length=250, db_index=True)
	files = models.CharField('Файл', max_length=250, default='', db_index=True)
	slug = models.SlugField('Порядковый номер', max_length=50, unique=True)
	gram = models.IntegerField('Вес', default=0)
	price = models.IntegerField('Цена', default=0)
	typebox = models.CharField('Тип упаковки', default='', max_length=250, db_index=True)
	lists = models.ManyToManyField('Sweets', related_name = 'sweets+', blank=True)

	def get_absolute_url(self):
		return reverse('cl_more_url', kwargs={'slug': self.slug})

	def __str__(self):
		return '{}'.format(self.title)

	class Meta:
		verbose_name = 'Список подарков серии "Классика"'
		verbose_name_plural = 'Классика'

class ClassicImg(models.Model):
	title = models.CharField('Название', max_length=250, default='', db_index=True)
	media = models.ImageField('Изображение', upload_to='classic', blank=True)

	def __str__(self):
		return "%s | %s" % (self.title, self.media)

	class Meta:
		verbose_name = 'Название | Изображение'
		verbose_name_plural = 'Изображения подарков серии "Классика"'

class Premium(models.Model):
	title = models.CharField('Название', max_length=250, db_index=True)
	series = models.CharField('Серия', max_length=50, default='Премиум', db_index=True)
	media = models.CharField('Изображение', max_length=250, db_index=True)
	files = models.CharField('Файл', max_length=250, default='', db_index=True)
	slug = models.SlugField('Порядковый номер', max_length=50, unique=True)
	gram = models.IntegerField('Вес', default=0)
	price = models.IntegerField('Цена', default=0)
	typebox = models.CharField('Тип упаковки', default='', max_length=250, db_index=True)
	lists = models.ManyToManyField('Sweets', related_name = 'sweets+', blank=True)

	def get_absolute_url(self):
		return reverse('pr_more_url', kwargs={'slug': self.slug})

	def __str__(self):
		return '{}'.format(self.title)

	class Meta:
		verbose_name = 'Список подарков серии "Премиум"'
		verbose_name_plural = 'Премиум'

class PremiumImg(models.Model):
	title = models.CharField('Название', max_length=250, default='', db_index=True)
	media = models.ImageField('Изображение', upload_to='premium', blank=True)

	def __str__(self):
		return "%s | %s" % (self.title, self.media)

	class Meta:
		verbose_name = 'Название | Изображение'
		verbose_name_plural = 'Изображения подарков серии "Премиум"'

class Sweets(models.Model):
	title = models.CharField('Название', max_length=250, db_index=True)
	descript = models.TextField('Описание', blank=True, db_index=True)
	manufact = models.CharField('Производитель', max_length=250, db_index=True)
	counts = models.IntegerField('Количество', blank=True, default=1)
	series = models.CharField('Серия', max_length=50, default='', db_index=True)
	number = models.CharField('Номер подарка', max_length=10, db_index=True)

	def __str__(self):
		return '{}'.format(self.title)

	class Meta:
		verbose_name = 'Список сладостей'
		verbose_name_plural = 'Сладости'

class SweetsImg(models.Model):
	title = models.CharField('Название', max_length=250, default='', db_index=True)
	media = models.ImageField('Изображение', upload_to='sweets', blank=True)

	def __str__(self):
		return '{}'.format(self.title)

	class Meta:
		verbose_name = 'Изображения'
		verbose_name_plural = 'Изображения сладостей'

class Manufactures(models.Model):
	title = models.CharField('Название', max_length=250, default='', db_index=True)
	media = models.ImageField('Изображение', upload_to='manufactures', blank=True)

	def __str__(self):
		return '{}'.format(self.title)

	class Meta:
		verbose_name = 'Изображения'
		verbose_name_plural = 'Изображения производителей'

class FilesLoad(models.Model):
	title = models.CharField('Название', max_length=250, default='', db_index=True)
	media = models.FileField('Файл', upload_to='files', blank=True)

	def __str__(self):
		return "%s | %s" % (self.title, self.media)

	class Meta:
		verbose_name = 'Название | Формат'
		verbose_name_plural = 'Файлы'

class Blocks(models.Model):
	title = models.CharField('Выделенный текст', max_length=250, default='', db_index=True)
	texts = models.TextField('Описание', blank=True, db_index=True)
	media = models.ImageField('Изображение', upload_to='blocks', blank=True)

	def __str__(self):
		return "%s | %s" % (self.id, self.title)

	class Meta:
		verbose_name = 'ID | Названия блоков'
		verbose_name_plural = 'Изображения блоков'

class TypeBox(models.Model):
	title = models.CharField('Тип упаковки', max_length=250, default='', db_index=True)
	media = models.ImageField('Изображение', upload_to='types', blank=True)

	def __str__(self):
		return "%s | %s" % (self.id, self.title)

	class Meta:
		verbose_name = 'ID | Тип упаковки'
		verbose_name_plural = 'Типы упаковок'

class Socials(models.Model):
	media = models.ImageField('Изображение', upload_to='socials', blank=True)
	urls = models.URLField('Ссылка', max_length=250, default='')

	def __str__(self):
		return '{}'.format(self.urls)

	class Meta:
		verbose_name = 'Социальные сети'
		verbose_name_plural = 'Социальные сети'

class Footer(models.Model):
	title1 = models.CharField('Заголовок 1', max_length=250, default='', db_index=True, blank=True)
	texts1 = models.TextField('Текст 1', db_index=True, blank=True)
	title2 = models.CharField('Заголовок 2', max_length=250, default='', db_index=True, blank=True)
	texts2 = models.TextField('Текст 2', db_index=True, blank=True)
	mail = models.CharField('Почта', max_length=250, default='@mail.ru', db_index=True, blank=True)
	copy = models.CharField('Копирайт', max_length=250, default='', db_index=True, blank=True)
	

	def __str__(self):
		return '{}'.format(self.copy)

	class Meta:
		verbose_name = 'Подвал сайта'
		verbose_name_plural = 'Подвал сайта'