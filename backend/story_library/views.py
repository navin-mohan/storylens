from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from pgvector.django import CosineDistance


from story_library.models import Story
from story_library.serializers import StorySerializer, SearchQuerySerializer

from llm.gemini import get_query_embedding, summarize_story, get_story_embedding

class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all().order_by('-created_at')
    serializer_class = StorySerializer

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data['summary'] = summarize_story(title=data['title'], story=data['story'])
        data['embedding'] = get_story_embedding(
            title=data['title'],
            story=data['story']
        )

        serializer = self.get_serializer(data=data)

        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
        self.perform_create(serializer)


        
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class SearchQueryAPI(APIView):
    def post(self, request):
        input_serializer = SearchQuerySerializer(data=request.data)

        print(input_serializer)

        if not input_serializer.is_valid():
            return Response(input_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        query_embedding = get_query_embedding(input_serializer.validated_data["query"])
        
        stories = Story.objects.order_by(CosineDistance('embedding', query_embedding))[:3]
        output_serializer = StorySerializer(stories, many=True)
        
        return Response(output_serializer.data)
