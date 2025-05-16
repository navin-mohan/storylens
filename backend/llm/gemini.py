from google import genai
from google.genai import types
from django.conf import settings

client = genai.Client(api_key=settings.GEMINI_API_KEY)




def summarize_story(title, story):
    response = client.models.generate_content(
        model=settings.GEMINI_TEXT_SUMMARIZATION_MODEL, 
        contents=f'Summarize the following story in 50 words. Title: "{title}" Story: {story}',
        config=types.GenerateContentConfig(
            max_output_tokens=200,
            temperature=0.1
        )
    )
    
    return response.text

def get_story_embedding(title, story):
    result = client.models.embed_content(
        model = settings.GEMINI_TEXT_EMBEDDING_MODEL,
        contents = f"title: {title} story: {story}",
        config=types.EmbedContentConfig(task_type="RETRIEVAL_DOCUMENT")
    )
    return result.embeddings[0].values

def get_query_embedding(query):
    result = client.models.embed_content(
        model=settings.GEMINI_TEXT_EMBEDDING_MODEL,
        contents=query,
        config=types.EmbedContentConfig(task_type="RETRIEVAL_QUERY")
    )
    return result.embeddings[0].values