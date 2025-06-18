from django.db import models

class ShortURL(models.Model):
    long_url = models.URLField()
    shortcode = models.CharField(max_length=15, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.shortcode} → {self.long_url}"
