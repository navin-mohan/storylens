from pgvector.django import VectorField
from django.db import models

from llm.gemini import get_story_embedding, summarize_story

class Story(models.Model):
    title = models.TextField()
    story = models.TextField()
    summary = models.TextField()
    author = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    embedding = VectorField(dimensions=768)

    def save(self, *args, **kwargs):
        self.embedding = get_story_embedding(
            title=self.title,
            story=self.story
        )
        self.summary = summarize_story(
            title=self.title,
            story=self.story
        )
        super().save(*args, **kwargs)
