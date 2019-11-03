from django.db import models

import PIL

from PIL import Image
from imagekit.models.fields import ImageSpecField
from imagekit.processors import ResizeToFit, Adjust,ResizeToFill


class Works(models.Model):
	my_works = models.TextField('Опыт работы')
	pub_date = models.DateTimeField('дата')
	def __str__(self):
		return self.my_works

	class Meta :
		verbose_name = 'Опыт работы'
		verbose_name_plural = 'Опыт работы'

class Program(models.Model):
	program_name = models.CharField('название программы', max_length = 200)
	program_text = models.TextField('текст программы')
	pub_date = models.DateTimeField('дата')


	def __str__(self):
		return self.program_name

	class Meta :
		verbose_name = 'Программы'
		verbose_name_plural = 'Программы'

class Hello_page(models.Model):
	hello_name = models.CharField('приветствие', max_length = 200)
	hello_text = models.TextField('приветствие')
	my_img = models.ImageField( 'Фото', upload_to='img', blank=False, null=True)

	def __str__(self):
		return self.hello_name

	class Meta :
		verbose_name = 'приветствие'
		verbose_name_plural = 'приветствие'