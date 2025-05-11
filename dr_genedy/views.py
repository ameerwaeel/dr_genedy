from .models import *
from .serializers import *
from django.conf import settings
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404 
from rest_framework import generics, status 
import threading
from django.core.mail import EmailMessage
import logging


logger = logging.getLogger(__name__)  

def send_form_email(subject, body, from_email, file_path=None):
    def send_email():
        try:
            email = EmailMessage(
                subject=subject,
                body=body,
                from_email=from_email,
                to=["mrseller.prof@gmail.com"],
            )
            if file_path:
                email.attach_file(file_path)
            email.send()
        except Exception as e:
            logger.error(f"Failed to send email: {e}")

    threading.Thread(target=send_email).start()


class create_appointmenListCreateView(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        subject = "موعد جديد تم حجزه"
        body = f"""
       الاسم: {instance.name}
       الهاتف: {instance.phone}
       التاريخ: {instance.date}
       الساعة: {instance.time}
        """
        success = send_form_email(subject, body, instance.name)

        if success:
            return Response({"message": "The active email has been sent!"}, status=status.HTTP_200_OK)
        return Response({"error": "An error occurred while sending the email."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class HomeVideoListCreateView(generics.ListCreateAPIView):
    queryset = HomeVideo.objects.all().order_by('-created_at')
    serializer_class = HomeVideoSerializer




class HomeArticleListCreateView(generics.ListCreateAPIView):
    queryset = HomeArticle.objects.all().order_by('-created_at')
    serializer_class = HomeArticleSerializer



class ContactUsListCreateView(generics.ListCreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        subject = f"رسالة جديدة من {instance.name} يريد التواصل معك"
        body = f"""
       الاسم: {instance.name}
       الهاتف: {instance.phone}
       الايميل : {instance.email}
       الرساله : {instance.message}
        """
        success = send_form_email(subject, body, instance.email)

        if success:
            return Response({"message": "The active email has been sent!"}, status=status.HTTP_200_OK)
        return Response({"error": "An error occurred while sending the email."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




class QuestionAnswerListCreateView(generics.ListCreateAPIView):
    queryset = QuestionAnswer.objects.all().order_by('-created_at')
    serializer_class = QuestionAnswerSerializer

