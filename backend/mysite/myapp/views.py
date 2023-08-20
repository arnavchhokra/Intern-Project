from django.shortcuts import render
from django.http import JsonResponse
import praw
from rest_framework.response import Response
from .serializers import ThreadSerializer
from rest_framework.views import APIView


class get_threads(APIView):
    def get(self, request, format=None):
        reddit = praw.Reddit(
        client_id='#',
        client_secret='#',
        user_agent='#'
        )
        subreddit = reddit.subreddit('AskReddit')
        threads = subreddit.new(limit=10)

        thread_data = []
        for thread in threads:
            thread_data.append({
                'title': thread.title,
                'author': thread.author.name,
                'url': thread.url
        })
    

        serializer = ThreadSerializer(thread_data, many=True)
        return Response(serializer.data)
    

