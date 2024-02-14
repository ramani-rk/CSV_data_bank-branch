from django.shortcuts import render

# Create your views here.

from app.models import *
from django.http import HttpResponse

import csv

def insert_bank (request):
    with open ('C:\\Users\\Ezhilkanthan\\OneDrive\\Desktop\\django projects\\django\\Scripts\\project39\\app\\bank.csv', 'r') as FO:
        IOD=csv.reader(FO)
        for id in IOD:
            bn=id[0].strip()
            BO=Bank(bname=bn)
            BO.save()
    return HttpResponse ('Bank Names are Inserted Successfully!!!!!')

def insert_branch (request):
    with open('C:\\Users\\Ezhilkanthan\\OneDrive\\Desktop\\django projects\\django\\Scripts\\project39\\app\\branch.csv','r') as FO:
        IOD=csv.reader(FO)
        next(IOD)
        for i in IOD:
            bn=i[0]
            BO=Bank.objects.filter(bname=bn)
            if BO:
                ifc=i[1]
                br=i[2]
                ad=i[3]
                co=i[4]
                ci=i[5]
                d=i[6]
                s=i[7]

                BRO=Branch(bname=BO[0],ifsc=ifc,branch=br,address=ad,contact=co,city=ci,district=d,state=s)
                BRO.save()
                
    
    return HttpResponse('Branch data is inserted successfully')