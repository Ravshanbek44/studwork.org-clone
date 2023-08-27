from .models import Question, Answer
from rest_framework import serializers
from user.serializers import SubjectSerializer


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['user', 'subject_question', 'question', 'image', 'views', 'is_answered', 'created_at',
                  'get_count_answers']


class QuestionListSerializer(serializers.ModelSerializer):
    subject_questions = SubjectSerializer()

    class Meta:
        model = Question
        fields = ['user', 'subject_questions', 'question', 'image', 'views', 'is_answered', 'created_at',
                  'get_count_answers']


class AnswerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Answer
        fields = ['user', 'question', 'image', 'answer']
