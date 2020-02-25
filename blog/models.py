from django.db import models
from django.contrib.auth.models import User
class blog(models.Model):
    image = models.ImageField(upload_to = 'images/')
    summary = models.TextField(max_length = 200)
    title = models.TextField(max_length = 200)
    time = models.DateTimeField()
    vote=models.IntegerField(default=0)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    def body(self):
        s=self.summary[0:12]+"................"
        return s
