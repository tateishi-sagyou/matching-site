from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse

class User(models.Model):
    user_id = models.CharField(verbose_name="ユーザーID",max_length=10,primary_key=True)
    user_name = models.CharField(verbose_name="ユーザー名",max_length=10)
    user_password = models.CharField(verbose_name="パスワード",max_length=10)
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.publish_date = timezone.now()
        self.save

    def __str__(self):
        return self.user_name

    def get_absolute_url(self):
        return reverse("login:create_done", kwargs={
            'user_id': self.user_id,
            'user_password': self.user_password,
            'user_name': self.user_name,
            })

    class Meta:
        verbose_name = "ユーザー"