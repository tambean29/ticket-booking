from django.db import models

from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {'Admin' if self.is_admin else 'User'}"
        
class Shows(models.Model):
    show_name = models.CharField(max_length=100, unique=True)
    show_time = models.TimeField()
    show_date = models.DateField()
    available_seats = models.IntegerField(default=100)

    def __str__(self):
        return self.show_name   