import datetime
from django.utils import timezone
from django.test import TestCase
from .models import Initiative

class InitiativeMethodTests(TestCase):

    def test_was_published_recently_with_future_initiative(self):
        """
        was_published_recently() should return False for initiatives whose pub_date in in the future
        """
        thefuture = timezone.now() + datetime.timedelta(days=30)
        future_initiative = Initiative(pub_date=thefuture)
        self.assertEqual(future_initiative.was_published_recently(), False)

    def test_was_published_recently_with_old_initiative(self):
        """
        was_published_recently() should return False for initiatives whose pub_date is older than 1 day
        """
        thepast = timezone.now() - datetime.timedelta(days=30)
        old_initiative = Initiative(pub_date=thepast)
        self.assertEqual(old_initiative.was_published_recently(), False)

    def test_was_published_recently_with_recent_initiative(self):
        """
        was_published_recently() should return True for initiatives whose pub_date is older than 1 day
        """
        recently = timezone.now() - datetime.timedelta(hours=1)
        recent_initiative = Initiative(pub_date=recently)
        self.assertEqual(recent_initiative.was_published_recently(), True)
