from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseServerError

import models
from POGOProtos.Networking.Envelopes_pb2 import RequestEnvelope
from POGOProtos.Networking.Envelopes_pb2 import ResponseEnvelope
from POGOProtos.Networking.Requests_pb2 import *
from POGOProtos.Networking import Responses_pb2
from POGOProtos.Networking.Requests import Messages_pb2
from google.protobuf import message

import re

# Create your views here.
def rpc(request, id='0'):
    print(sys.stderr, 'URL ID: ' + id)
    if re.search("com.nianticlabs.pokemongo", request.META['HTTP_USER_AGENT']):

        mesg = Request.FromString(request.body, id='0')

        if mesg.RequesType.name == "GET_PLAYER":
            # TODO do something if RequestType is GET_PLAYER
            try:
                data = mesg.RequestMesg
                respon = Responses_pb2._GETPLAYERRESPONSE()
                respon.result = True
                return HttpResponse(respon.SerializeToString(), content_type="application/octet-stream")
            except:
                return HttpResponseServerError
        elif mesg.RequesType.name == "GET_PLAYER_PROFILE":
            # TODO do something if RequestType is GET_PLAYER_PROFILE
            try:
                data = mesg.RequestMesg
                respon = Responses_pb2._GETPLAYERPROFILERESPONSE()
                player = models.Player.objects.get(username=data.username())
                respon.start_time = player.creation_timestamp_ms
                respon.badges = player.equippedbadge_set
                respon.result = True
                return HttpResponse(respon.SerializeToString(), content_type="application/octet-stream")
            except:
                return HttpResponseServerError

        else:
            print(sys.stderr, 'Unimplemented message: ' + mesg.RequestType.name)
            return HttpResponseServerError
    if id!='0':
        return HttpResponse("Your not playing Pokemon Go, but your ID from the URL is " + id)
    else:
        return HttpResponse("Your not playing Pokemon Go")

def dumbdumb(request):
    return HttpResponse("Nothing to see here dumb dumb")