from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from test_api_app import serializer



class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializer.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})


    def post(self, request):
        """Create a hello message with our name"""
        serializerr = self.serializer_class(data=request.data)

        if serializerr.is_valid():
            name = serializerr.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message':message})
        else:
            return Response(serializerr.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """ Handle a partial update of an object"""
        return Response({'method':'PATCH'})


    def delete(self, request, pk=None):
        """Delete an Object"""
        return Response({'method':'DELETE'})
