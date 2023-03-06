from django.core.validators import FileExtensionValidator
from django.db import models

# В шаблон для видео
# <video width="500px" height="500px" controls>
#      <source src="{{ post.video_file.url }}" type="video/mp4">
# </video>


# Create your models here.
class MainPageVideo(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    video_path = models.FileField(
        upload_to='patient/video',
        validators=[FileExtensionValidator(allowed_extensions=['mp4'])]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
