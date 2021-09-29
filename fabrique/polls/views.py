from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Poll, Question, Answer
from .serializers import PollSerializer, QuestionSerializer, AnswerSerializer


class PollsView(APIView):
    def get(self, request):
        polls = Poll.objects.all()
        serializer = PollSerializer(polls, many=True)
        return Response({"polls": serializer.data})

    def post(self, request):
        polls = request.data.get("polls")
        serializer = PollSerializer(data=polls)
        if serializer.is_valid(raise_exception=True):
            poll_saved = serializer.save()
        return Response({"success": "Poll '{}' created successfully".format(poll_saved.title)})


class QuestionsView(APIView):
    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response({"questions": serializer.data})

    def post(self, request):
        questions = request.data.get("questions")
        serializer = QuestionSerializer(data=questions)
        if serializer.is_valid(raise_exception=True):
            question_saved = serializer.save()
        return Response({"success": "Question '{}' created successfully".format(question_saved.title)})


class AnswersView(APIView):
    def get(self, request):
        answers = Answer.objects.all()
        serializer = AnswerSerializer(answers, many=True)
        return Response({"answer": serializer.data})

    def post(self, request):
        answers = request.data.get("answer")
        serializer = AnswerSerializer(data=answers)
        if serializer.is_valid(raise_exception=True):
            answer_saved = serializer.save()
        return Response({"success": "Answer '{}' created successfully".format(answer_saved.title)})
