from django.db import models




class Customer(models.Model):
    
    customer = models.CharField(max_length = 100)

class UserLocation(models.Model):
    
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Location ({self.latitude}, {self.longitude})"
