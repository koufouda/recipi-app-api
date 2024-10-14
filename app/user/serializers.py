"""
Serializes for the user API
"""

from django.contrib.auth import get_user_model

from rest_framework import serializers

class user_serialiser (serializers.ModelSerializer):
    """Serializer for the user model"""

    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'name']
        extra_Kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create (self, validation_data):
        """Create user and return it"""
        return get_user_model().objects.create_user(**validation_data)
