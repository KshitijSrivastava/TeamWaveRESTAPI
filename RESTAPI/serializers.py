from rest_framework import serializers
from RESTAPI.models import UserData, Question, Answer

class UserSerializer(serializers.ModelSerializer):
     class Meta:
        model = UserData
        fields = ['display_name', 'user_type', 'reputation']


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        depth = 2
        #fields = '__all__'
        fields = ['title', 'question_text', 'creation_date', 'is_answered', 'question_user']

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['question', 'answer_user', 'text', 'created_date']


class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        depth = 2
        fields = '__all__'
