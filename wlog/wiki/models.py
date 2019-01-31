from django.db import models
import datetime
# Create your models here.

class Post(models.Model):
    is_active = models.BooleanField(default = True)
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    title = models.CharField(max_length = 200)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now = False, auto_now_add = True, null = True)
    updated_at = models.DateTimeField(auto_now = True, auto_now_add = False, null = True)

    def publish(self):
        self.updated_at = datetime.datetime.now()
        self.save()

    def __str__(self):
        return self.title
    