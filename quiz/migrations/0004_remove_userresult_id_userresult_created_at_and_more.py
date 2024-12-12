# Generated by Django 5.1.4 on 2024-12-12 11:28

import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_rename_user_id_quizsession_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userresult',
            name='id',
        ),
        migrations.AddField(
            model_name='userresult',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userresult',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='userresult',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
    ]