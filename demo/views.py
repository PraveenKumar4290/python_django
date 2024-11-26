from django.shortcuts import render
from rest_framework.response import Response # type: ignore
from rest_framework.decorators import api_view # type: ignore
from rest_framework.generics import GenericAPIView # type: ignore
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin  # type: ignore
from .models import *
from .serializer import *

class StudentList(GenericAPIView,ListModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    def get(self,request):
        return self.list(request)
    
class StudentGetById(GenericAPIView,RetrieveModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    def  get(self,request,**kwargs):
        return self.retrieve(request,**kwargs)
    
class StudentAdd(GenericAPIView,CreateModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    def post(self,request):
        return self.create(request)

class StudentUpdate(GenericAPIView,UpdateModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    def put(self,request,**kwargs):
        return self.update(request,**kwargs)
    
class StudentDelete(GenericAPIView,DestroyModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    def delete(self,request,**kwargs):
        return self.destroy(request,**kwargs)
  
# Create your views here.
# @api_view(['GET'])
# def home(request):
#     student=Student.objects.all()
#     sez_students=StudentSerializer(student,many=True)
#     return Response({'status':200,'message':'Successfully done','obj_response':sez_students.data})


# @api_view(['POST'])
# def add_student(request):
#     student=StudentSerializer(data=request.data)
#     if student.is_valid():
#         student.save()
#         return Response({'status':200,'message':'Successfully Created','obj_response':student.data})
#     else:
#         raise ValueError('Something went wrong')
    
    
# @api_view(['PUT'])
# def update_student(request,id):
#     student=Student.objects.get(id=id)
#     sez_student=StudentSerializer(instance=student,data=request.data)
#     if sez_student.is_valid():
#         sez_student.save()
#         return Response({'status':200,'message':'Successfully Updated','obj_response':sez_student.data})
#     else:
#         raise ValueError('Something went wrong')
    
    
# @api_view(['DELETE'])
# def delete_student(request,id):
#     student=Student.objects.get(id=id)
#     if student is not None:
#         student.delete()
#         return Response({'status':200,'message':'Successfully Deleted'})
#     else:
#         raise ValueError('Something went wrong')
