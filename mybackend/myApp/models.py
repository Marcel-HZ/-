from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class FisherMan(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField("姓名", max_length=20, default="")
    phone = models.CharField("电话", max_length=11)
    email = models.EmailField("邮箱", max_length=50)
    create_time = models.DateTimeField("创建时间", auto_now_add=True)

    class Meta:
        ordering = ['id']
        db_table = 'fisherman'
        verbose_name = '养殖户'
        verbose_name_plural = '养殖户'

    def __str__(self):
        return self.name


