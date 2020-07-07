from rest_framework import serializers


class BaseSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'created_by': {'write_only': True},
            'updated_by': {'write_only': True},
            'deleted_by': {'write_only': True},
        }


class BaseUserSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'user': {'write_only': True},
            'created_by': {'write_only': True},
            'updated_by': {'write_only': True},
            'deleted_by': {'write_only': True},
        }
