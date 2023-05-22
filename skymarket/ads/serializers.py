from rest_framework import serializers

from .models import Ad, Comment


# TODO Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою


class CommentSerializer(serializers.ModelSerializer):
    author_id = serializers.IntegerField(source='author.id', read_only=True)
    ad_id = serializers.IntegerField(source='ad.id', read_only=True)
    author_first_name = serializers.CharField(source='author.first_name', read_only=True)
    author_last_name = serializers.CharField(source='author.last_name', read_only=True)
    author_image = serializers.ImageField(source='author.image', read_only=True)

    class Meta:
        model = Comment
        fields = (
            'pk',
            'text',
            'author_id',
            'created_at',
            'author_first_name',
            'author_last_name',
            'ad_id',
            'author_image'
        )
        # fields = (
        #     'pk',
        #     'text',
        #     'author_id',
        #     'ad_id',
        #     'author_first_name',
        #     'author_last_name',
        #     'author_image'
        # )


class AdSerializer(serializers.ModelSerializer):
    author_id = serializers.IntegerField(source='author.id', read_only=True)
    author_first_name = serializers.CharField(source='author.first_name', read_only=True)
    author_last_name = serializers.CharField(source='author.last_name', read_only=True)
    phone = serializers.CharField(source='author.phone', read_only=True)

    class Meta:
        model = Ad
        fields = (
            'pk',
            'title',
            'description',
            'author_id',
            'price',
            'author_first_name',
            'author_last_name',
            'image',
            'phone',
        )


# class AdDetailSerializer(serializers.ModelSerializer):
#     author_first_name = serializers.CharField(source='author.first_name')
#     author_last_name = serializers.CharField(source='author.last_name')
#     author_id = serializers.CharField(source='author.id')
#
#     # def get_author_first_name(self, obj):
#     #     return obj.author.first_name
#     #
#     # def get_author_last_name(self, obj):
#     #     return obj.author.last_name
#     #
#     # def get_author_id(self, obj):
#     #     return obj.author.id
#
#     class Meta:
#         model = Ad
#         fields = ('pk', 'title', 'price', 'author', 'author_first_name')
