from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'admin/pages/dashboard.html')


def miners(request):
    return render(request, 'admin/pages/miners.html')


def atlas(request):
    return render(request, 'admin/pages/atlas.html')


def power(request):
    return render(request, 'admin/pages/power.html')


def alphamatic(request):
    return render(request, 'admin/pages/alphamatic.html')


def activity(request):
    return render(request, 'admin/pages/activity.html')


def rewards(request):
    return render(request, 'admin/pages/rewards.html')


def payouts(request):
    return render(request, 'admin/pages/payouts.html')


def reporting(request):
    return render(request, 'admin/pages/reporting.html')
