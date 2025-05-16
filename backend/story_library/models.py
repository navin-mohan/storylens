from pgvector.django import VectorField
from django.db import models

class Story(models.Model):
    title = models.TextField()
    story = models.TextField()
    summary = models.TextField()
    author = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    embedding = VectorField(dimensions=768)
