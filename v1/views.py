from django.shortcuts import render
from django.http import HttpResponse

from POGOProtos.Networking.Envelopes_pb2 import RequestEnvelope
from POGOProtos.Networking.Envelopes_pb2 import ResponseEnvelope
from POGOProtos.Networking.Requests_pb2 import RequestType
from POGOProtos.Networking.Requests import Messages_pb2
from google.protobuf import message

# Create your views here.
def login(request):
    mesg = Messages_pb2(request.body)
    return HttpResponse("Hi, you're trying to login.")

def dumbdumb(request):
    return HttpResponse("Nothing to see here dumb dumb")