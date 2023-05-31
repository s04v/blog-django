from django.db import models

class Post(models.Model):
  id = models.AutoField(primary_key=True)
  title = models.CharField('Post title', max_length=100)
  text = models.TextField('Post text')
  date = models.DateField('Date', auto_now_add=True)

  def __str__(self):
    return f'{self.title}'

  class Meta: 
    verbose_name = 'Post'
    verbose_name_plural = 'Post'