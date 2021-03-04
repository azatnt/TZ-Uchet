from rest_framework import serializers
from Task.models import *
from django.contrib.auth.models import User





class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'



class RegisterSerializer(serializers.ModelSerializer):
        def save(self):
            user = User(
                email=self.validated_data['email'],
                username=self.validated_data['username'],
            )
            e_mail = self.validated_data['email']
            if User.objects.filter(email=e_mail).count()>0:
                raise serializers.ValidationError({'email': 'User with that email already exists'})
            user.set_password(self.validated_data['password'])
            user.save()
            return user

        email = serializers.EmailField()

        class Meta:
            model = User
            fields = ['username', 'email', 'password']
            extra_kwargs = {
                'password': {'write_only': True},
                'email': {'required': False}
            }



class UserPasswordChangeSerializer(serializers.ModelSerializer):
    profile = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name', 'profile')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.username = validated_data['username']
        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        email = validated_data['email']
        if User.objects.filter(email=email).count() > 0:
            raise serializers.ValidationError("Email already exists")
        else:
            instance.email = email
        instance.save()
        return instance

    def create(self, validated_data):
        pass

        return Response(data)
