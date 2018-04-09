from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Stations,PoliceEntry
from . serializers import StationsSerializer
from . serializers import UserSerializer
from . serializers import PoliceEntrySerializer




class StationsList(APIView):
    def get(self, request):
        stations1 = Stations.objects.all()
        serializer = StationsSerializer(stations1, many = True)
        return Response(serializer.data)

    def post(self, request):
        pass
        # sobj = StationsSerializer(data = request.data)
        # print(sobj)
        # if sobj.is_valid():
        #     sobj.save()
        # return Response()


class PoliceEntrys(APIView):
    def get(self, request):
        policeEntry1 = PoliceEntry.objects.all()
        serializer = PoliceEntrySerializer(policeEntry1, many = True)
        return Response(serializer.data)

    def post(self):
        pass
        # pobj = PoliceEntrySerializer(data = request.data)
        # print(pobj)
        # if pobj.is_valid():
        #     pobj.save()
        # return Response()




class UserList(APIView):
    def get(self, request):
        user1 = User_Request.objects.all()
        serializer = UserSerializer(user1, many = True)
        return Response(serializer.data)

    def post(self):
        pass

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def PoliceListEntry(request):
    if request.method == "POST":
        policeID = request.POST.get('policeID')
        password = request.POST.get('password')
        station = request.POST.get('station')
        Name = request.POST.get('PoliceName')
        ForceID = request.POST.get('ForceId')
        Batchno = request.POST.get('BatchNo')
        ContactNo = request.POST.get('ContactNo')
        station_ref = Stations.objects.get(stationID__exact = station)
        p = PoliceEntry(
        policeID = policeID,
        password = password,
        # data = policeData,
        station = station_ref,
        PoliceName = Name,
        ForceId = ForceID,
        BatchNo = Batchno,
        ContactNo = ContactNo
        )
        p.save()
        return HttpResponse('Successfully Inserted Police')
    else:
        return HttpResponse('')





# @csrf_exempt
# def savePolice(request):
#     if request.method == "POST":
#         policeID = request.POST.get('policeID')
#         policeData = request.POST.get('data')
#         station = request.POST.get('station')
#         station_ref = Stations.objects.get(stationID__exact = station)
#         p = Policemen(
#         policeID = policeID,
#         data = policeData,
#         station = station_ref
#         )
#         p.save()
#         return HttpResponse('Successfully Inserted Police')
#     else:
#         return HttpResponse('')






@csrf_exempt
def policeStation(request):
    if request.method == 'POST':
        stationID = request.POST.get('stationID')
        stationName = request.POST.get('stationName')
        stationDistrict = request.POST.get('district')
        stationCoordinates = request.POST.get('coordinates')
        stationData = request.POST.get('data')
        s = Stations(
        stationID = stationID,
        stationName = stationName,
        district = stationDistrict,
        coordinates = stationCoordinates
    )
        s.save()
        return HttpResponse('Successfully Inserted Stations')
    else:
        return HttpResponse('')







@csrf_exempt
def UserRequest(request):
    if request.method == 'POST':
        RequestID = request.POST.get('RequestID')
        Details = request.POST.get('Details')
        Coordinates = request.POST.get('Coordinates')
        RegisteredNo = request.POST.get('RegisteredNo')
        UserName = request.POST.get('UserName')
        AadhaarID = request.POST.get('AadhaarID')
        Image = request.POST.get('Image')
        u = User_Request(
        RequestID = RequestID,
        Details = Details,
        Coordinates = Coordinates,
        RegisteredNo = RegisteredNo,
        UserName = UserName,
        AadhaarID = AadhaarID,
        Image = Image
    )
        u.save()
        return HttpResponse('Successfully Inserted Request')
    else:
        return HttpResponse('')




