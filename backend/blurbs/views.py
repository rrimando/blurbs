from django.shortcuts import render
from rest_framework.parsers import JSONParser

# To Bypass CSRF
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse, JsonResponse
from .serializers import BlurbSerializer
from .models import Blurb


@csrf_exempt
def blurbs(request):
    """
    All Blurbs
    """
    if request.method == "GET":
        blurbs = Blurb.objects.all()
        serializer = BlurbSerializer(blurbs, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = BlurbSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def blurb_details(request, pk):
    try:
        blurb = Blurb.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)
    if request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = BlurbSerializer(blurb, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == "DELETE":
        blurb.delete()
        return HttpResponse(status=204)
