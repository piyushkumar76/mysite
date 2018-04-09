from rest_framework import serializers
from . models import User_Request, Stations, PoliceEntry
#from . models import Policemen


class StationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stations
        fields = '__all__'




# class PolicemenSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Policemen
#         fields = '__all__'
#


class PoliceEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = PoliceEntry
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Request
        fields = '__all__'
