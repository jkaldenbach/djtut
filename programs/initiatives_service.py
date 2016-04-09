import datetime
from django.utils import timezone
from .models import Initiative, Program

def get_active_initiatives():
        now = timezone.now()
        return Initiative.objects.filter(start_date__lte=now, end_date__gte=now)
