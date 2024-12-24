from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    CLIENT = 'client'
    PARTNER = 'partner'
    ROLE_CHOICES = [
        (CLIENT, "Client"),
        (PARTNER, 'Partner')
    ]

    role = models.CharField(max_length=7, choices=ROLE_CHOICES)


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    text = models.TextField()
    rating = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    partner_response = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Review of {self.product.name} by {self.user.username}'
    

class Notification(models.Model):
    INFORMATIVE = 'informative'
    ATTENTION = 'attention'
    CRITICAL = 'critical'
    LEVEL_CHOICES = [
        (INFORMATIVE, 'Informative'),
        (ATTENTION, 'Attention'),
        (CRITICAL, 'Critical')
    ]

    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    text = models.TextField()
    level = models.CharField(max_length=12, choices=LEVEL_CHOICES, default=INFORMATIVE)

    def __str__(self):
       return f'Notification for {self.recipient.username} ({self.get_level_display()})'