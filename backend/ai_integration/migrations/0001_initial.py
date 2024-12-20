# Generated by Django 5.0 on 2024-12-17 09:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AIPromptTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('prompt_text', models.TextField()),
                ('analysis_type', models.CharField(choices=[('grammar', 'Grammar Check'), ('pronunciation', 'Pronunciation Analysis'), ('writing', 'Writing Evaluation'), ('speaking', 'Speaking Evaluation')], max_length=20)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='AIAnalysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('analysis_type', models.CharField(choices=[('grammar', 'Grammar Check'), ('pronunciation', 'Pronunciation Analysis'), ('writing', 'Writing Evaluation'), ('speaking', 'Speaking Evaluation')], max_length=20)),
                ('input_text', models.TextField()),
                ('input_audio', models.FileField(blank=True, null=True, upload_to='ai_analysis/audio/')),
                ('result', models.JSONField()),
                ('feedback', models.TextField()),
                ('score', models.FloatField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ai_analyses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AIFeedbackHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_text', models.TextField()),
                ('is_helpful', models.BooleanField(null=True)),
                ('user_comment', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('analysis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedback_history', to='ai_integration.aianalysis')),
            ],
        ),
    ]
