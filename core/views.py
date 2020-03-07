from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.


def index(request):
    """
    Return the index page
    :param request:
    :return: view
    """
    return render(request, 'core/pages/root.html')


def sign_in(request):
    """
    Return sign in page
    :param request:
    :return: view
    """
    return render(request, 'core/pages/sign_in.html')


def sign_up(request):
    """
    Return sign up page
    :param request:
    :return: view
    """
    return render(request, 'core/pages/sign_up.html')



def privacy(request):
    """
    Return privacy page
    :param request:
    :return: view
    """
    return render(request, 'core/pages/privacy.html')


def tnc(request):
    return render(request, 'core/pages/tnc.html')

def mining_pools(request):
    return render(request, 'core/pages/mining_pools.html')

def gdpr(request):
    return render(request, 'core/pages/gdpr.html')

def hash_market(request):
    return render(request, 'core/pages/hash_market.html')

def staking_pools(request):
    return render(request, 'core/pages/staking_pools.html')

def statistics(request):
    return render(request, 'core/pages/statistics.html')

def my_account(request):
    return render(request, 'core/pages/my_account.html')

def getting_started(request):
    return render(request, 'core/pages/getting_started.html')

def how_to_mine(request):
    return render(request, 'core/pages/how_to_mine.html')

def how_to_buy(request):
    return render(request, 'core/pages/how_to_buy.html')

def how_to_stake(request):
    return render(request, 'core/pages/how_to_stake.html')

def atomic_swaps(request):
    return render(request, 'core/pages/atomic_swaps.html')

def announcements(request):
    return render(request, 'core/pages/announcements.html')

def faq(request):
    return render(request, 'core/pages/faq.html')

def about_us(request):
    return render(request, 'core/pages/about_us.html')

def careers(request):
    return render(request, 'core/pages/careers.html')

def partners(request):
    return render(request, 'core/pages/partners.html')

def open_a_ticket(request):
    return render(request, 'core/pages/open_a_ticket.html')

def contact(request):
    return render(request, 'core/pages/contact.html')

def visit_out_friends(request):
    return render(request, 'core/pages/visit_out_friends.html')

def alpha_vertical(request):
    return render(request, 'core/pages/alpha_vertical.html')

def atlash(request):
    return render(request, 'core/pages/atlash.html')

def swan_bitcoin(request):
    return render(request, 'core/pages/swan_bitcoin.html')

def blockchain_inst(request):
    return render(request, 'core/pages/blockchain_inst.html')
