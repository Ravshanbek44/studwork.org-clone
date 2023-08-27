from .models import WorkType, Work, Comment, FileWork, MyTakenWork, OtClick
from rest_framework import serializers
from user.serializers import SubjectSerializer, UserSerializer


class WorkTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkType
        fields = ['id', 'name']


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ['id', 'user', 'name', 'work_type', 'specialist', 'deadline', 'hours', 'description', 'price',
                  'is_faster', 'views', 'is_open']


class WorkFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileWork
        fields = ['id', 'file']


class WorkListSerializer(serializers.ModelSerializer):
    work_types = WorkTypeSerializer()
    work_specialist = SubjectSerializer()
    files_work = WorkFileSerializer(many=True)

    class Meta:
        model = Work
        fields = ['id', 'user', 'name', 'work_types', 'work_specialist', 'deadline', 'hours', 'description', 'price',
                  'is_faster', 'views', 'is_open', 'get_doer', 'get_comment_count', 'get_click', 'files_work']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'work', 'user', 'message']


class OtClickSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtClick
        fields = ['id', 'work', 'user']


class CreateOtClickSerializer(serializers.ModelSerializer):
    want_work = UserSerializer()

    class Meta:
        model = OtClick
        fields = ['id', 'work', 'want_work']


class TakenWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyTakenWork
        fields = ['id', 'doer', 'work']


class MyWorkSerializer(serializers.ModelSerializer):
    doer_work = WorkSerializer(many=True)

    class Meta:
        model = MyTakenWork
        fields = ['id', 'doer', 'doer_work']
