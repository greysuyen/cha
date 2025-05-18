from django.shortcuts import render
import datetime

def index(request):
    now = datetime.datetime.now()
    hour = now.hour
    return render(request, "sched/index.html",{
        "sched":(0 <= hour <= 6) or (17 <= hour <= 23)
    })
