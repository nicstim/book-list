from rest_framework import serializers

from book.models import Profile, Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Book


class ProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Profile


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["is_visible"]
        model = Profile

    def to_representation(self, instance):
        serializer = ProfileListSerializer(instance, context={"request": self.context["request"]})
        return serializer.data
