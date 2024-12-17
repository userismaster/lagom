from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import User

class Course(models.Model):
    LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    thumbnail = models.ImageField(upload_to='courses/thumbnails/')
    duration = models.DurationField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_free = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Lesson(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='lessons'
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    content = models.TextField()
    order = models.IntegerField()
    duration = models.DurationField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.course.title} - {self.title}"

class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField()
    thumbnail = models.ImageField(upload_to='videos/thumbnails/')
    duration = models.DurationField()
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    is_free = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Podcast(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    audio_file = models.FileField(upload_to='podcasts/')
    thumbnail = models.ImageField(upload_to='podcasts/thumbnails/')
    duration = models.DurationField()
    created_at = models.DateTimeField(auto_now_add=True)
    plays = models.IntegerField(default=0)
    is_free = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class UserCourseProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    completed_lessons = models.ManyToManyField(Lesson)
    last_accessed = models.DateTimeField(auto_now=True)
    progress_percentage = models.FloatField(default=0)

    class Meta:
        unique_together = ['user', 'course']

    def __str__(self):
        return f"{self.user.username} - {self.course.title}"

class UserVideoProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    watched_duration = models.DurationField(default=0)
    last_watched = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)

    class Meta:
        unique_together = ['user', 'video']

class UserPodcastProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE)
    listened_duration = models.DurationField(default=0)
    last_listened = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)

    class Meta:
        unique_together = ['user', 'podcast']
