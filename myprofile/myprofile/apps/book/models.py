from django.db import models

import PIL

from PIL import Image
from imagekit.models.fields import ImageSpecField
from imagekit.processors import ResizeToFit, Adjust,ResizeToFill

class Books(models.Model):
	books_name = models.CharField('название учебника', max_length = 200)
	linck_book = models.CharField('ссылка на учебник', max_length = 200)
	book_img = models.ImageField( 'обложка', upload_to='img', blank=False, null=True)

	def __str__(self):
		return self.books_name

	class Meta :
		verbose_name = 'название учебника'
		verbose_name_plural = 'название учебника'