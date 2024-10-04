from django.contrib import admin
from .models import Candidates, VoteTotal

# Register your models here.

#displaying all candidates

admin.site.register(Candidates)
admin.site.register(VoteTotal)