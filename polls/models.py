from django.db import models
from django.contrib.auth.models import User

class Candidates(models.Model):
    image = models.ImageField(upload_to='images/')
    Name = models.CharField(max_length=100)
    age = models.IntegerField()
    position = models.CharField(max_length=100)
    party = models.CharField(max_length=100)
    total_votes = models.IntegerField(default=0)  # Field to store total votes for the candidate

    def __str__(self):
        return self.Name


class VoteTotal(models.Model):
    Name = models.ForeignKey(Candidates, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} voted for {self.Name}"
