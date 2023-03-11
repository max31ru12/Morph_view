from django.core.validators import FileExtensionValidator
from django.db import models

# В шаблон для видео
# <video width="500px" height="500px" controls>
#      <source src="{{ post.video_file.url }}" type="video/mp4">
# </video>


# Create your models here.
class MainPageVideo(models.Model):
    title = models.CharField(max_length=128, verbose_name='Название видео')
    description = models.TextField(verbose_name='Описание видео')
    video_path = models.FileField(
        upload_to='patient/video/',
        validators=[FileExtensionValidator(allowed_extensions=['mp4'])],
        verbose_name='Путь'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')
    is_published = models.BooleanField(default=False, verbose_name='Добавлено на страницу')

    def __str__(self):
        return self.title
