from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView


from RESTAPI.models import UserData, Question, Answer
from RESTAPI.serializers import AnswerSerializer, QuestionSerializer, UserSerializer
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
    serializer_class = QuestionSerializer

    def get_queryset(self):
        return Question.objects.all()

    def filter_queryset(self, queryset):

        queryset = self.get_queryset()
        for ques in queryset:
            print(ques.question_user)
        print('params', self.request.query_params)
        return queryset

    # def get_object(self):
    #     queryset = self.get_queryset()
    #     filter = {}
    #     for field in self.multiple_lookup_fields:
    #         filter[field] = self.kwargs[field]
    #
    #     print('filter', filter)
    #     print('kwargs', self.kwargs)
    #     print('querry param', self.request.query_params)
    #     return queryset


def home(request):
    return HttpResponse('Welcome to REST API')
