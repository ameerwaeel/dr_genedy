from django.db import models

class Appointment(models.Model):
    name = models.CharField(max_length=255,null=False, blank=False)
    phone = models.CharField(max_length=20,null=False, blank=False)
    date = models.DateField(null=False, blank=False)
    time = models.TimeField(null=False, blank=False)
    is_available = models.BooleanField(default=True)
    reason_if_rejected = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.date} at {self.time}"
    
class ClosedSlot(models.Model):
    date = models.DateField()
    time = models.TimeField(blank=True, null=True)  
    reason = models.CharField(max_length=255)

    def __str__(self):
        return f"Closed: {self.date} - {self.time or 'Full Day'}"
    
class HomeVideo(models.Model):
    name = models.CharField(max_length=255,null=False, blank=False)
    video = models.FileField(upload_to='videos/',null=False, blank=False)
    image = models.ImageField(upload_to='video_thumbnails/',null=False, blank=False)
    link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class HomeArticle(models.Model):
    name = models.CharField(max_length=255,null=False, blank=False)
    image = models.ImageField(upload_to='articles/',null=False, blank=False)
    link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ContactUs(models.Model):
    name = models.CharField(max_length=255,null=False, blank=False)
    phone = models.CharField(max_length=20,null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    message = models.TextField(blank=True, null=True)
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"


class QuestionAnswer(models.Model):
    question = models.TextField(null=False, blank=False)
    answer = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question[:50]
    
