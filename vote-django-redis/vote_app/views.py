from django.shortcuts import render
from redis import Redis
import os
import socket
import random
import json
import logging

option_a = os.getenv('OPTION_A', "Cats")
option_b = os.getenv('OPTION_B', "Dogs")
hostname = socket.gethostname()


def home(request):
    print(request.build_absolute_uri()) #optional
    voter_id = request.COOKIES.get('voter_id')
    if not voter_id:
        voter_id = hex(random.getrandbits(64))[2:-1]
    vote = None
    return render(
        request,
        'vote_app/index.html',
        {
            "option_a": option_a,
            "option_b": option_b,
            "hostname": hostname,
            "vote": vote,
        }
    )