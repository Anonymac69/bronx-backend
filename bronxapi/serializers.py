from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Article



class ArticleSerializer(serializers.Serializer):
  id = serializers.IntegerField(read_only=True)
  title = serializers.CharField(max_length=200)
  content = serializers.CharField()
  author = serializers.CharField(max_length=200)
  email = serializers.CharField(max_length=200)

  class Meta:
    fields = ['id', 'title', 'content', 'author', 'email']

  def create(self, validated_data):
    return Article.objects.create(**validated_data)

  def update(self, instance, validated_data):
    instance.title = validated_data.get('title', instance.title)
    instance.content = validated_data.get('content', instance.content)
    instance.author = validated_data.get('author', instance.author)
    instance.email = validated_data.get('email', instance.email)
    instance.save()
    return instance


class ArticleModelSerializer(serializers.ModelSerializer):
  # id = serializers.IntegerField(read_only=True)
  title = serializers.CharField(
    max_length=200,
    validators=[UniqueValidator(
      queryset=Article.objects.all(),
      message='An article with that name already exists.',
      lookup='iexact',
    )]
  )
  # content = serializers.CharField()
  # author = serializers.CharField(max_length=200)
  # email = serializers.CharField(max_length=200)

  class Meta:
    model = Article
    fields = ['id', 'title', 'content', 'author', 'email']






