from djongo import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    class Meta:
        app_label = 'core'
    
    def __str__(self):
        return self.name

class Activity(models.Model):
    name = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    duration = models.IntegerField()
    
    class Meta:
        app_label = 'core'
        verbose_name_plural = 'Activities'
    
    def __str__(self):
        return f"{self.name} - {self.user} ({self.duration}min)"

class Leaderboard(models.Model):
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    
    class Meta:
        app_label = 'core'
        ordering = ['-points']
    
    def __str__(self):
        return f"{self.team}: {self.points} points"

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    class Meta:
        app_label = 'core'
    
    def __str__(self):
        return self.name
