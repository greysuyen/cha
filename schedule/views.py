from django.shortcuts import render
import datetime

def index(request):
    now = datetime.datetime.now()
    return render(request, "sched/index.html",{
        "sched": now.hour == 15
    })
