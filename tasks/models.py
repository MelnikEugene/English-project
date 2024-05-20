from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    example = models.TextField()

class Solution(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    text = models.TextField()
    
class Word(models.Model):
    russian = models.CharField(max_length=100)
    english = models.CharField(max_length=100)

    def __str__(self):
        return self.russian
