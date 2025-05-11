from django.urls import path
from .views import *

urlpatterns = [
    path('appointments/', create_appointmenListCreateView.as_view(), name='appointments'),
    path('videos/', HomeVideoListCreateView.as_view(), name='videos'),
    path('articles/', HomeArticleListCreateView.as_view(), name='articles'),
    path('ContactUs/', ContactUsListCreateView.as_view(), name='ContactUs'),
    path('Question&Answer/', QuestionAnswerListCreateView.as_view(), name='Question&Answer'),


]
