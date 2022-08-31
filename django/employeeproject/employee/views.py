from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ViewSet
from employee.serializers import EmployeeSerializer
from rest_framework.response import Response
from employee.models import Emp

class EmployeeView(ViewSet):
    def list(self,request,*args,**kwargs):
        qs=Emp.objects.all()
        serializers=EmployeeSerializer(qs,many=True)
        return Response(data=serializers.data)

    def create(self,request,*args,**kwargs):
        serializer=EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def retrieve(self,request,*args,**kwargs):
        id =kwargs.get("pk")
        qs=Emp.objects.get(id=id)
        serializer=EmployeeSerializer(qs)
        return Response(data=serializer.data)

    def update(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        instance = Emp.objects.get(id=id)
        serializer = EmployeeSerializer(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def destroy(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        instance = Emp.objects.get(id=id)
        instance.delect()
        return Response({"msg": "deleted"})