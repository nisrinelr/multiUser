from rest_framework import serializers
from gallery.models import Image
from rest_framework.exceptions import AuthenticationFailed

class ImagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id','title', 'description', 'image')
    def validate(self, attrs):
        owner = self.context['request'].user
        if owner.is_anonymous:
            raise AuthenticationFailed("Authentication credentials were not provided.")
        return super().validate(attrs)
    def create(self, validated_data):
        owner = self.context['request'].user
        validated_data['owner'] = owner
        return super().create(validated_data)