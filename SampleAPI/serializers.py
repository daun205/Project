from django.contrib.auth.models import User, Group
from .models import Post
from rest_framework import serializers






import logging

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		# fields = (
		# 	'id',
		# 	'user',
		# 	'message'
		# 	)
		fields = '__all__'

	def create(self, validated_data):
		logging.warning("ENTERED CREWATE")
		user = self.context['request'].user
		logging.warning("###################################")
		logging.warning(user)
		logging.warning("###################################")
		message = validated_data.pop('message')
		newPost = Post.objects.create(message=message, user=user)
		return newPost

	# def validate(self,data):
		# user = self.context['request'].user
		# if user