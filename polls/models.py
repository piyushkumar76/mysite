from django.db import models



class User_Request(models.Model):
    RequestID = models.CharField(max_length=100, primary_key= True)
    Details = models.CharField(max_length=2000,null=True)
    Coordinates = models.CharField(max_length=50,null=True)
    RegisteredNo = models.CharField(max_length=15,null=True)
    UserName = models.CharField(max_length=50,null=True)
    AadhaarID = models.CharField(max_length=50, null=True)
    Image = models.CharField(max_length=1000000, null=True)

    def __str__(self):
        return self.RequestID

class Stations(models.Model):
    StationID = models.CharField(max_length=100, primary_key= True)
    StationName = models.CharField(max_length=200)
    District = models.CharField(max_length=200)
    Coordinates = models.CharField(max_length=200)
    Data = models.CharField(max_length=2000,null=True)
    def __str__(self):
        return self.StationID



class PoliceEntry(models.Model):
    PoliceID = models.CharField(max_length=200, primary_key = True)
    Password = models.CharField(max_length=200)
    PoliceName = models.CharField(max_length=200)
    ForceId = models.CharField(max_length=200, unique=True)
    BatchNo = models.CharField(max_length=200)
    ContactNo = models.CharField(max_length=10)
    Station = models.ForeignKey(Stations, on_delete = models.CASCADE)
    def __str__(self):
        return self.ForceId
