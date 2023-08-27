# import serializers from the REST framework
from rest_framework import serializers

# import the todo data model
from admin_app.models import profile

# create a serializer class
class LoginSerializer(serializers.ModelSerializer):

	# create a meta class
	class Meta:
		model = profile
		fields = ('username','password')
