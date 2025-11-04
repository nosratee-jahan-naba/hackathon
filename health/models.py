from django.db import models

# Create your models here.
from django.db import models

class HealthCheck(models.Model):
    user_name = models.CharField(max_length=255)
    mood = models.IntegerField(choices=[(1, 'Bad'), (2, 'Okay'), (3, 'Good'), (4, 'Great')])
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name} - {self.mood}"
