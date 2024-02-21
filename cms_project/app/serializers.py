from rest_framework import serializers
from .models import Author, Category, Content

class AuthorSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True) 

    class Meta:
        model = Author
        fields = ('id', 'full_name', 'email', 'phone', 'address', 'city', 'state', 'country', 'pincode', 'password') 

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = Author(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class ContentSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True)

    class Meta:
        model = Content
        fields = ('id', 'title', 'body', 'summary', 'categories', 'author', 'created_at', 'updated_at')
