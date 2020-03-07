from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # App Navigation URL's
    path('sign_in', views.sign_in, name='login'),
    path('sign_up', views.sign_up, name='register'),
    path('privacy', views.privacy, name='privacy'),
    path('tnc', views.tnc, name='tnc'),
    path('mining_pools', views.mining_pools, name='mining_pools'),
    path('gdpr', views.gdpr, name='gdpr'),
    path('hash_market', views.hash_market, name='hash_market'),
    path('staking_pools', views.staking_pools, name='staking_pools'),
    path('statistics', views.statistics, name='statistics'),
    path('my_account', views.my_account, name='my_account'),
    path('getting_started', views.getting_started, name='getting_started'),
    path('how_to_mine', views.how_to_mine, name='how_to_mine'),
    path('how_to_buy', views.how_to_buy, name='how_to_buy'),
    path('how_to_stake', views.how_to_stake, name='how_to_stake'),
    path('atomic_swaps', views.atomic_swaps, name='atomic_swaps'),
    path('announcements', views.announcements, name='announcements'),
    path('faq', views.faq, name='faq'),
    path('about_us', views.about_us, name='about_us'),
    path('careers', views.careers, name='careers'),
    path('partners', views.partners, name='partners'),
    path('open_a_ticket', views.open_a_ticket, name='open_a_ticket'),
    path('contact', views.contact, name='contact'),
    path('visit_out_friends', views.visit_out_friends, name='visit_out_friends'),
    path('alpha_vertical', views.alpha_vertical, name='alpha_vertical'),
    path('atlash', views.atlash, name='atlash'),
    path('swan_bitcoin', views.swan_bitcoin, name='swan_bitcoin'),
    path('blockchain_inst', views.blockchain_inst, name='blockchain_inst'),
]
