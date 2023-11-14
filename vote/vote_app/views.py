from django.shortcuts import render
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache
import os
import json
import socket
import random


option_a = os.getenv('OPTION_A', "Cats")
option_b = os.getenv('OPTION_B', "Dogs")
hostname = socket.gethostname()


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@cache_page(CACHE_TTL)
def home(request):
    
    data = {}
    
    voter_id = request.COOKIES.get('voter_id')
    if not voter_id:
        voter_id = hex(random.getrandbits(64))[2:-1]

    vote = None

    if request.method == 'POST':
        vote = request.POST.get('vote')
        data = json.dumps({'voter_id': voter_id, 'vote': vote})
        cache.set('votes', data)

    resp = render(
        request,
        'vote_app/index.html',
        {
            "option_a": option_a,
            "option_b": option_b,
            "hostname": hostname,
            "vote": vote,
        }
    )

    resp.set_cookie('voter_id', voter_id)
    return resp