from django.shortcuts import render
from userpost.models import UserPost
from userpost.serializer import UserPostSerializer
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

class UserPostViewSet(viewsets.ModelViewSet):
    queryset = UserPost.objects.all().order_by('pk')
    serializer_class = UserPostSerializer

    filter_backends = [SearchFilter]
    search_fields = ('title', 'body',)





    def get_queryset(self):
        qs = super().get_queryset()
        # qs = qs.filter(author__id = 1) 
        if self.request.user.is_authenticated:
            qs = qs.filter(author=self.request.user)
        else:
            qs = qs.none()

        return qs
