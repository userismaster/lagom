from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import User

class IELTSTest(models.Model):
    TEST_TYPES = [
        ('academic', 'Academic'),
        ('general', 'General Training'),
    ]

    title = models.CharField(max_length=200)
    test_type = models.CharField(max_length=20, choices=TEST_TYPES)
    description = models.TextField()
    duration = models.DurationField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_mock = models.BooleanField(default=False)
    is_free = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} ({self.test_type})"

class Section(models.Model):
    SECTION_TYPES = [
        ('listening', 'Listening'),
        ('reading', 'Reading'),
        ('writing', 'Writing'),
        ('speaking', 'Speaking'),
    ]

    test = models.ForeignKey(
        IELTSTest,
        on_delete=models.CASCADE,
        related_name='sections'
    )
    section_type = models.CharField(max_length=20, choices=SECTION_TYPES)
    title = models.CharField(max_length=200)
    instructions = models.TextField()
    duration = models.DurationField()
    total_questions = models.IntegerField()
    passing_score = models.FloatField()

    def __str__(self):
        return f"{self.test.title} - {self.get_section_type_display()}"

class Question(models.Model):
    QUESTION_TYPES = [
        ('multiple_choice', 'Multiple Choice'),
        ('true_false', 'True/False'),
        ('fill_blank', 'Fill in the Blank'),
        ('matching', 'Matching'),
        ('essay', 'Essay'),
        ('speaking', 'Speaking Response'),
    ]

    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        related_name='questions'
    )
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES)
    text = models.TextField()
    instructions = models.TextField()
    points = models.FloatField(default=1.0)
    order = models.IntegerField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.section.title} - Question {self.order}"

class Choice(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='choices'
    )
    text = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.question} - Choice: {self.text[:30]}"

class UserTestAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(IELTSTest, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    total_score = models.FloatField(null=True, blank=True)
    
    class Meta:
        unique_together = ['user', 'test', 'start_time']

    def __str__(self):
        return f"{self.user.username} - {self.test.title}"

class UserAnswer(models.Model):
    attempt = models.ForeignKey(
        UserTestAttempt,
        on_delete=models.CASCADE,
        related_name='answers'
    )
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text_answer = models.TextField(null=True, blank=True)
    selected_choices = models.ManyToManyField(Choice, blank=True)
    score = models.FloatField(null=True, blank=True)
    feedback = models.TextField(null=True, blank=True)

    class Meta:
        unique_together = ['attempt', 'question']

    def __str__(self):
        return f"{self.attempt} - {self.question}"
