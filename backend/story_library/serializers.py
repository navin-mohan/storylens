from rest_framework import serializers

from story_library.models import Story

class SearchQuerySerializer(serializers.Serializer):
    query = serializers.CharField()

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = [
            'id',
            'story',
            'title',
            'author',
            'summary',
            'embedding'
        ]

        extra_kwargs = {
            'id': {
                'read_only' : True
            },
            'created_at': {
                'read_only' : True
            },
            'summary': {
                'read_only' : True
            },
            'embedding': {
                'read_only' : True 
            }
        }