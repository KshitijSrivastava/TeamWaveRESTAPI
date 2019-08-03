from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView


from RESTAPI.throttles import BurstRateThrottle, SustainedRateThrottle
from RESTAPI.models import UserData, Question, Answer
from RESTAPI.serializers import AnswerSerializer, QuestionSerializer, UserSerializer, QuerySerializer
# Create your views here.

class StandardResultsPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 1000

class UserList(generics.ListCreateAPIView):
    queryset = UserData.objects.all()
    serializer_class = UserSerializer
    pass

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserData.objects.all()
    serializer_class = UserSerializer

class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class AnswerList(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class AnswerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class Search(generics.ListAPIView):
    pagination_class = StandardResultsPagination
    serializer_class = QuerySerializer
    throttle_classes = [BurstRateThrottle, SustainedRateThrottle]


    def get_queryset(self):
        return Question.objects.all()

    def filter_queryset(self, queryset):

        queryset = self.get_queryset()
        params = self.request.query_params

        filters_query = {}
        if 'id' in params:
            filters_query['id'] = int(params['id'])
        if 'title' in params:
            filters_query['title'] = params['title']
        # if 'accepted' in params:
        #     filters_query['accepted'] = params['accepted']

        queryset = queryset.filter(**filters_query)
        return queryset

    #@method_decorator(cache_page(60*60*2))
    # def get(self, request, format=None):
    #     super().get(self, request, format = None)

def home(request):
    return HttpResponse('Welcome to REST API')
