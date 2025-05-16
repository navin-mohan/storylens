from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from pgvector.django import CosineDistance


from story_library.models import Story
from story_library.serializers import StorySerializer, SearchQuerySerializer

from llm.gemini import get_query_embedding

class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all().order_by('-created_at')
    serializer_class = StorySerializer

class SearchQueryAPI(APIView):
    def post(self, request):
        input_serializer = SearchQuerySerializer(data=request.data)

        print(input_serializer)

        if not input_serializer.is_valid():
            return Response(input_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        query_embedding = get_query_embedding(input_serializer.validated_data["query"])
        
        stories = Story.objects.order_by(CosineDistance('embedding', query_embedding))[:10]
        output_serializer = StorySerializer(stories, many=True)
        
        return Response(output_serializer.data)
