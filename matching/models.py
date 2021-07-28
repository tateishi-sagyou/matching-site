from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse

class User(models.Model):
    user_id = models.CharField(verbose_name="ユーザーID",max_length=10,primary_key=True,null=False)
    user_password = models.CharField(verbose_name="パスワード",max_length=10,null=False)
    delete_flg = models.BooleanField(verbose_name="削除フラグ",null=True)
    created_date = models.DateTimeField(verbose_name="作成日時",default=timezone.now,null=False)
    delete_date = models.DateTimeField(verbose_name="削除日時",null=True)


    def publish(self):
        self.publish_date = timezone.now()
        self.save


    def get_absolute_url(self):
        return reverse("login:create_done", kwargs={
            'user_id': self.user_id,
            'user_password': self.user_password,
            })

    class Meta:
        verbose_name = "ユーザー"

class UserDetail(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,primary_key=True)
    user_name = models.CharField(verbose_name="ユーザー名",max_length=10,null=True)
    user_age = models.CharField(verbose_name="年齢",max_length=2,null=True)
    user_sex_cd = models.CharField(verbose_name="性別種別コード",max_length=2,null=True)
    user_profile = models.TextField(verbose_name='プロフィール',max_length=200,null=True)
    group_flg = models.BooleanField(verbose_name="団体フラグ",null=True)
    sports_kind_cd = models.CharField(verbose_name="スポーツ種別コード",max_length=2,null=True)
    delete_flg = models.BooleanField(verbose_name="削除フラグ",null=True)
    created_date = models.DateTimeField(verbose_name="作成日時",default=timezone.now)
    delete_date = models.DateTimeField(verbose_name="削除日時",null=True)

class UserImage(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    user_images = models.ImageField(verbose_name = 'イメージ',upload_to='image/')
    delete_flg = models.BooleanField(verbose_name="削除フラグ",null=True)
    created_date = models.DateTimeField(verbose_name="作成日時",default=timezone.now)
    delete_date = models.DateTimeField(verbose_name="削除日時",null=True)

class UserLike(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    to_like_user_id = models.CharField(verbose_name="いいねしたユーザーID",max_length=10)
    delete_flg = models.BooleanField(verbose_name="削除フラグ",null=True)
    created_date = models.DateTimeField(verbose_name="作成日時",default=timezone.now)
    delete_date = models.DateTimeField(verbose_name="削除日時",null=True)

class ChatRoom(models.Model):
    room_id = models.AutoField(verbose_name="ルームID",primary_key=True,max_length=10)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    partner_user_id = models.CharField(verbose_name="会話相手ユーザーID",max_length=10)
    chat = models.CharField(verbose_name="会話内容",max_length=170)
    delete_flg = models.BooleanField(verbose_name="削除フラグ",null=True)
    created_date = models.DateTimeField(verbose_name="作成日時",default=timezone.now)
    delete_date = models.DateTimeField(verbose_name="削除日時",null=True)

