import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from task.models import Task
from user.models import User


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


#
# class TaskSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Task
#         fields = ['title', 'description', 'cat']
#
#
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

#
# class TaskModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content
#
#
# class TaskerSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()
#
#
# def encode():
#     model = TaskModel('Do you homework', 'Content: dance dance dance')
#     model_sr = TaskerSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
#
# def decode():
#     stream = io.BytesIO(b'{"title":"Do you homework","content":"Content: dance dance dance"}')
#     data = JSONParser().parse(stream)
#     serializer = TaskerSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
