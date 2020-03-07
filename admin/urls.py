from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='dashboard'),

    # App Navigation URL's
    path('miners', views.miners, name='miners'),
    path('atlas', views.atlas, name='atlas'),
    path('power', views.power, name='power'),
    path('alphamatic', views.alphamatic, name='alphamatic'),
    path('activity', views.activity, name='activity'),
    path('rewards', views.rewards, name='rewards'),
    path('payouts', views.payouts, name='payouts'),
    path('reporting', views.reporting, name='reporting'),
]