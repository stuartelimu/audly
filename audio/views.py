from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def home(request):
    return HttpResponse("Hello world!")

@csrf_exempt
def webhook(request):
    req = json.loads(request.body)
    action = req.get('queryResult').get('parameters')
    print(action)
    fullfillmentText = {'fulfillmentText': 'This is a test response from Django webhook'}
    return JsonResponse(fullfillmentText, safe=False)

