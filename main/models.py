from django.db import models

class Excursion(models.Model):
    title = models.CharField('Название экскурсии', max_length=100)
    desc = models.TextField('Описание экскурсии')
    time = models.TimeField('Время начала экскурсии')
    pict = models.ImageField(upload_to='pictures', default=None, blank=True,
                             null=True, verbose_name="Фото")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Экскурсия'
        verbose_name_plural = 'Экскурсии'

    def get_absolute_url(self):
        return '../excursions'