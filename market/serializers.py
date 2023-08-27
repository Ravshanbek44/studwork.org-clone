from rest_framework import serializers
from .models import Market, MarketFileDemo, MarketFileDone


class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = ['id', 'user', 'name', 'work_type', 'specialist', 'uni_name', 'course', 'description', 'content',
                  'list_lit', 'is_top']


class MarketFileDemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketFileDemo
        fields = ['id', 'market', 'file']


class MarketFileDoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketFileDone
        fields = ['id', 'market', 'file']


class MarketListSerializer(serializers.ModelSerializer):
    file_demo = MarketFileDemoSerializer(many=True, required=False)
    file_done = MarketFileDoneSerializer(many=True, required=False)

    class Meta:
        model = Market
        fields = ['id', 'user', 'name', 'work_type', 'specialist', 'uni_name', 'course', 'description', 'content',
                  'list_lit', 'is_top', 'file_demo', 'file_done']
