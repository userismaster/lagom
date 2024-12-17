from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import User

class AIAnalysis(models.Model):
    ANALYSIS_TYPES = [
        ('grammar', 'Grammar Check'),
        ('pronunciation', 'Pronunciation Analysis'),
        ('writing', 'Writing Evaluation'),
        ('speaking', 'Speaking Evaluation'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='ai_analyses'
    )
    analysis_type = models.CharField(max_length=20, choices=ANALYSIS_TYPES)
    input_text = models.TextField()
    input_audio = models.FileField(upload_to='ai_analysis/audio/', null=True, blank=True)
    result = models.JSONField()
    feedback = models.TextField()
    score = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.get_analysis_type_display()}"

class AIPromptTemplate(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    prompt_text = models.TextField()
    analysis_type = models.CharField(max_length=20, choices=AIAnalysis.ANALYSIS_TYPES)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.get_analysis_type_display()}"

class AIFeedbackHistory(models.Model):
    analysis = models.ForeignKey(
        AIAnalysis,
        on_delete=models.CASCADE,
        related_name='feedback_history'
    )
    feedback_text = models.TextField()
    is_helpful = models.BooleanField(null=True)
    user_comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback for {self.analysis}"
