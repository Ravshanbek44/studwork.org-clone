from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import Account, VerifyPhone, Subject, SubjectType


class SubjectTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectType
        fields = ['id', 'name']


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=64, min_length=4, write_only=True)

    class Meta:
        model = Account
        fields = ['id', 'phone', 'username', 'password']


class LoginSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(max_length=20, required=True)
    password = serializers.CharField(max_length=64)

    class Meta:
        model = Account
        fields = ['phone', 'password']

    # def validate(self, attrs):
    #     phone = attrs.get('phone')
    #     password = attrs.get('password')
    #     print(password)
    #     user = Account.objects.filter(phone=phone).first()
    #     if not user:
    #         raise serializers.ValidationError({'success': False, 'message': 'User not found'})
    #     if not user.is_verified:
    #         raise serializers.ValidationError({'message': 'user is not verified'})
    #     if user:
    #         authenticate(phone=phone, password=password)
    #     data = {
    #         'phone': user.phone,
    #         'password': user.password
    #     }
    #     return data


class VerifySerializer(serializers.ModelSerializer):
    class Meta:
        model = VerifyPhone
        fields = '__all__'


class ResetPasswordSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=14)
    password = serializers.CharField(max_length=100)


class VerifyRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=64, min_length=4, write_only=True)

    class Meta:
        model = VerifyPhone
        fields = ('phone', 'code', 'password')


class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(max_length=64, write_only=True)
    password = serializers.CharField(max_length=64, write_only=True)

    class Meta:
        model = Account
        fields = ['password', 'old_password']

    def validate(self, attrs):
        old_password = attrs.get('old_password')
        password = attrs.get('password')
        request = self.context.get('request')
        try:
            user = request.user
        except:
            raise serializers.ValidationError({'message': 'User not found'})

        if not user.check_password(old_password):
            raise serializers.ValidationError({'message': 'Old password not match'})

        user.set_password(password)
        user.save()
        return attrs

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'phone', 'username', 'image', 'bio', 'user_status', 'specialist']
