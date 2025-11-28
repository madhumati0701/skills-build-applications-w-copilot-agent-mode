from django.contrib import admin
from core.models import Team, Activity, Leaderboard, Workout

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'user', 'team', 'duration']
    list_filter = ['team', 'name']
    search_fields = ['name', 'user', 'team']

@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ['id', 'team', 'points']
    list_filter = ['team']
    ordering = ['-points']

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    search_fields = ['name', 'description']
