from rest_framework import serializers
from .models import *
from datetime import date
from django.utils import timezone

class AppointmentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True, allow_blank=False)
    phone = serializers.CharField(required=True, allow_blank=False)
    date = serializers.DateField(required=True, allow_null=False)
    time = serializers.TimeField(required=True, allow_null=False)
    reason_if_rejected = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = Appointment
        fields = ['name', 'phone', 'date', 'time','reason_if_rejected' ]

    def validate(self, data):
        date_ = data['date']
        time_ = data['time']

        # اليوم في الماضي
        if date_ < date.today():
            raise serializers.ValidationError("لا يمكن اختيار يوم في الماضي")

        # تحقق من غلق اليوم بالكامل
        if ClosedSlot.objects.filter(date=date_, time__isnull=True).exists():
            raise serializers.ValidationError("هذا اليوم مغلق بالكامل")

        # تحقق من غلق الساعة
        if ClosedSlot.objects.filter(date=date_, time=time_).exists():
            raise serializers.ValidationError("هذا التوقيت مغلق")

        # تحقق من وجود موعد سابق بنفس التاريخ والساعة
        if Appointment.objects.filter(date=date_, time=time_).exists():
            raise serializers.ValidationError("تم حجز هذا الموعد بالفعل")

        for field in ['name', 'phone', 'date', 'time' ]:
            if not data.get(field):
                raise serializers.ValidationError({field: "This field is required."})

        return data

class HomeVideoSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True, allow_blank=False)
    # video = serializers.FileField(required=True, allow_null=False)
    image = serializers.ImageField(required=True, allow_null=False)

    class Meta:
        model = HomeVideo
        fields = [
            'name',
            # 'video',
            'image',
            'link'
            ]

    def validate(self, data):
        if not data.get('name'):
            raise serializers.ValidationError({"name": "هذا الحقل مطلوب"})
        # if not data.get('video'):
        #     raise serializers.ValidationError({"video": "هذا الحقل مطلوب"})
        if not data.get('image'):
            raise serializers.ValidationError({"image": "هذا الحقل مطلوب"})

        return data


class HomeArticleSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True, allow_blank=False)
    image = serializers.ImageField(required=True, allow_null=False)

    class Meta:
        model = HomeArticle
        fields = ['name', 'image', 'link']

    def validate(self, data):
        if not data.get('name'):
            raise serializers.ValidationError({'name': 'الاسم مطلوب'})
        if not data.get('image'):
            raise serializers.ValidationError({'image': 'الصورة مطلوبة'})

        return data

class ContactUsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True, allow_blank=False)
    phone = serializers.CharField(required=True, allow_blank=False)
    email = serializers.EmailField(required=True, allow_blank=False)
    class Meta:
        model = ContactUs
        fields = ['name', 'phone', 'email', 'message']

    def validate(self, data):
        if not data.get('name'):
            raise serializers.ValidationError({'name': 'الاسم مطلوب'})
        if not data.get('phone'):
            raise serializers.ValidationError({'phone': 'رقم الهاتف مطلوب'})
        if not data.get('email'):
            raise serializers.ValidationError({'email': 'البريد الإلكتروني مطلوب'})
        return data

class QuestionAnswerSerializer(serializers.ModelSerializer):
    question = serializers.CharField(required=True, allow_blank=False)
    answer = serializers.CharField(required=True, allow_blank=False)
    class Meta:
        model = QuestionAnswer
        fields = ['question', 'answer']
    def validate(self, data):
        if not data.get('question'):
            raise serializers.ValidationError({'question': 'السؤال مطلوب'})
        if not data.get('answer'):
            raise serializers.ValidationError({'answer': 'الإجابة مطلوبة'})
        return data
