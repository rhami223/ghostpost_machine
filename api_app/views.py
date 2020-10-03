from django.shortcuts import render
from .serializers import BoastRoastSerializer
from api_app import models
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response 
from rest_framework.parsers import JSONParser
from django.db.models import F




class BoastRoastViewSets(viewsets.ModelViewSet):
    queryset = models.BoastRoast.objects.all()
    serializer_class = BoastRoastSerializer

    def create(self, request):
        postdata = JSONParser().parse(request)
        print(postdata)
        postserializer = BoastRoastSerializer(data=postdata['data'])
        print(postserializer)
        if postserializer.is_valid():
            postserializer.save()
            return Response({'status': 'success'})
        return Response({'status': 'failure'})

    @action(detail=False)
    def Boast(self, request):
        Boast = models.BoastRoast.objects.filter(isroast=False).order_by('-submissiondate')
        serializer = self.get_serializer(Boast, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def Roast(self, request):
        Roast = models.BoastRoast.objects.filter(isroast=True).order_by('-submissiondate')
        serializer = self.get_serializer(Roast, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def Hghest(self, request):
        post = models.BoastRoast.objects.order_by(-(F('upvotes') - F('downvotes')))
        serializer = self.get_serializer(post, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def upvotes(self, request, pk=None):
        post = self.get_object()
        post.upvotes += 1
        post.save()
        return Response({'status': 'upvotes'})

    @action(detail=True, methods=['post'])
    def downvotes(self, request, pk=None):
        post = self.get_object()
        post.downvotes += 1
        post.save()
        return Response({'status': 'downvotes'})