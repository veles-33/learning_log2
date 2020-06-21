from django.db import models

class Topic(models.Model):
	"""Тема, которую изучает пользователь."""

	title = models.CharField(max_length=200, verbose_name='Рубрика')
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'Рубрики'
		verbose_name = 'Рубрика'

	def __str__(self):
		"""Возвращает строковое предстовление модели."""
		return self.title


class Entry(models.Model):
	"""Информация, изученая пользователем по теме."""

	topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'Записи'

	def __str__(self):
		"""Возвращает строковое предстовление модели."""
		return self.text[:50] + '...'
