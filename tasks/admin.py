from django.contrib import admin
from .models import Task, Solution
from .models import Word

admin.site.register(Word)
admin.site.register(Task)
admin.site.register(Solution)
