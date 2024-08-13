from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Stock(models.Model):
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    date = models.DateField()
    def __str__(self):
        return self.name



class StockMetadata(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    market_cap = models.BigIntegerField()
    sector = models.CharField(max_length=100)
    headquarters = models.CharField(max_length=100)


class HistoricalPrice(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    price = models.FloatField()
    date = models.DateField()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    favorite_stocks = models.ManyToManyField('Stock', related_name='favorited_by')
    def __str__(self):
        return self.user.username
    
class Comment(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}: {self.text[:50]}...'
