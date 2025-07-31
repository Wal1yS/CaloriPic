from django.db import models

class Articles(models.Model):
    title = models.CharField('Name', max_length=200)
    content = models.TextField('Content')
    date = models.DateTimeField('Date')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}/'

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ['-date']