from django.test import TestCase
from pgvector.django import CosineDistance

from story_library.models import Story

class SimilaritySearchTest(TestCase):
    def setUp(self):
        Story.objects.create(
            title="This is a Title",
            story="This is the content of the story.",
            author="Author Name",
            summary="This is the summary",
            embedding=[0] * 768,
            id=1
        )

        Story.objects.create(
            title="This is a Title",
            story="This is the content of the story.",
            author="Author Name",
            summary="This is the summary",
            embedding=[1] * 768,
            id=2
        )

    def test_similarity_search(self):
        query_embedding = [2] * 768
        stories = Story.objects.order_by(CosineDistance('embedding', query_embedding))[:10]
        
        self.assertEqual(stories[0].id, 2)
        self.assertEqual(stories[1].id, 1)
