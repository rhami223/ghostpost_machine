from rest_framework import serializers
from api_app import models
class BoastRoastSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.BoastRoast
        fields = [
            'id',
            'isroast',
            'post_content',
            'upvotes',
            'downvotes',
            'submissiondate',
            'score'
        ]