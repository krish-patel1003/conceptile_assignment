# Generated by Django 5.1.4 on 2024-12-12 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_remove_userresult_id_userresult_created_at_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userattempt',
            unique_together={('quiz_session_id', 'question_id')},
        ),
    ]
