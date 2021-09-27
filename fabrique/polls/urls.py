from django.urls import path
from .views import PollsView, QuestionsView, AnswersView

app_name = "polls"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('polls/', PollsView.as_view()),
    path('questions/', QuestionsView.as_view()),
    path('answers/', AnswersView.as_view()),
]