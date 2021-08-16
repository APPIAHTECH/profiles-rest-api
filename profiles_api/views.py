from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiView( APIView ):

    def get(self , req, format=None):
        an_apiview = [
            'Uses http methods as fun (get, post, patch, put, delete)',
            'Is similiar to a traditional django view',
            'Is mapped manually yo URLs'
        ]

        return Response({
            'message': 'Hey',
            'an_apiview': an_apiview
        })

    def post(self , req, format=None): pass
    def put(self , req, format=None): pass
    def patch(self , req, format=None): pass
    def delete(self , req, format=None): pass
    
