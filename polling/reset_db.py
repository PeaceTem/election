from .models import *
from datetime import datetime


def test():
    alr = polling_unit.objects.all()
    for a in alr:
        a.date_entered = datetime.now()
        a.save()
