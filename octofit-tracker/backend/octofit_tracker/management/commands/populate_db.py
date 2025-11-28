from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from core.models import Team, Activity, Leaderboard, Workout

User = get_user_model()

class Command(BaseCommand):
    """Populate the octofit_db database with test data"""
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear collections
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password')
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='password')

        # Create activities
        Activity.objects.create(name='Running', user='ironman', team='Marvel', duration=30)
        Activity.objects.create(name='Swimming', user='batman', team='DC', duration=45)

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=100)
        Leaderboard.objects.create(team='DC', points=80)

        # Create workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups')
        Workout.objects.create(name='Situps', description='Do 30 situps')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
