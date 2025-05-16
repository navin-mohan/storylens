from django.urls import include, path
from rest_framework import routers

from story_library.views import StoryViewSet, SearchQueryAPI

router = routers.DefaultRouter()

router.register(r'stories', StoryViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('query', SearchQueryAPI.as_view(), name="query")
]