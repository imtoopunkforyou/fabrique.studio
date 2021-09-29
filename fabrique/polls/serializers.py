from rest_framework import serializers


class PollSerializer(serializers.Serializer):
    title = serializers.CharField()
    poll_start = serializers.DateField()
    poll_end = serializers.DateField()


class QuestionSerializer(serializers.Serializer):
    type = serializers.CharField()
    question = serializers.CharField()


class AnswerSerializer(serializers.Serializer):
    answer = serializers.CharField()
