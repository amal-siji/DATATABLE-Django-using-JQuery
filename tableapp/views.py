from django.shortcuts import redirect, render
from django.core.paginator import Paginator
# Create your views here.
from rest_framework import status
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.serializers import *
from django.shortcuts import render
from rest_framework import generics
from tableapp.forms import Editform
from .serializers import *
from . models import *
from django.views.generic import ListView
from .models import *
from django.views import View
# Create your views here.


def perview(request):
    people = Person.objects.all()
    context = {
        'show_peoples': people}
    return render(request, "person.html", context)


def Edit_per(request, id):
    per = Person.objects.get(id=id)
    form = Editform(instance=per)
    if request.method == 'POST':
        form = Editform(request.POST, instance=per)
        if form.is_valid():
            form.save()
            return redirect('view')

    context = {'form': form, 'id': id}
    return render(request, 'edit.html', context)


def del_per(request, id):
    book = Person .objects.get(id=id)
    book.delete()
    return redirect('view')


class push(generics.CreateAPIView):

    serializer_class = table_serializer
    queryset = Person.objects.all()

    def post(self, request):
        serializer = table_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('view')
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
