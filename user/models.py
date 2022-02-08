from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 100)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=15)
    username = models.CharField(max_length=50)
    def __str__(self):
        return str(self.id) + " " + self.username
class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

