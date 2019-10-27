from .models import Post, Files, Album
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):

    author_name = serializers.ReadOnlyField(source='author.username')


    class Meta:
        model = Post
        fields = ('pk', 'title', 'body', 'author_name')

class AlbumSerializer(serializers.ModelSerializer):

    author_name = serializers.ReadOnlyField(source='author.username')
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Album
        # fields = '__all__'
        fields = ('pk', 'image', 'desc', 'author_name')

class FilesSerializer(serializers.ModelSerializer):

    author = serializers.ReadOnlyField(source='author.username')
    myfile = serializers.FileField(use_url=True)

    class Meta:
        model = Files
        # fields = '__all__'
        fields = ('pk', 'myfile', 'desc', 'author')
