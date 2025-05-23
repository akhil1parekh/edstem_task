from django.db import models
from django.contrib.auth.models import User


class Activity(models.Model):
    EVENT_TYPE = [
        ("page_view", "Page View"),
        ("click", "Click"),
        ("form_submit", "FOrm Submit"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_type = models.CharField(choices=EVENT_TYPE, max_length=20)
    timestamp = models.DateTimeField()
    page = models.CharField(max_length=127, blank=True)
    browser = models.CharField(max_length=127, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.event_type}"
