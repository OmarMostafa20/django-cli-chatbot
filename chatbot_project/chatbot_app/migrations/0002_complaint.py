# Generated by Django 5.0.1 on 2024-01-25 12:42

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.TextField()),
                ('complaint_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatbot_app.customer')),
            ],
        ),
    ]
