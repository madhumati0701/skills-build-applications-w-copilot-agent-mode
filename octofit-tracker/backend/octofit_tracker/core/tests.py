from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from core.models import Team, Activity, Leaderboard, Workout

User = get_user_model()

class TeamAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.team = Team.objects.create(name='Test Team')

    def test_get_teams(self):
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_team(self):
        self.client.force_authenticate(user=self.user)
        data = {'name': 'New Team'}
        response = self.client.post('/api/teams/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ActivityAPITestCase(APITestCase):
    def setUp(self):
        self.activity = Activity.objects.create(
            name='Running',
            user='testuser',
            team='Test Team',
            duration=30
        )

    def test_get_activities(self):
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class LeaderboardAPITestCase(APITestCase):
    def setUp(self):
        self.leaderboard = Leaderboard.objects.create(team='Test Team', points=100)

    def test_get_leaderboard(self):
        response = self.client.get('/api/leaderboard/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class WorkoutAPITestCase(APITestCase):
    def setUp(self):
        self.workout = Workout.objects.create(name='Pushups', description='Do 20 pushups')

    def test_get_workouts(self):
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
