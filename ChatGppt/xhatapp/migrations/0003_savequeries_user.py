# Generated by Django 4.1 on 2023-05-04 14:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("xhatapp", "0002_savequeries_query_time"),
    ]

    operations = [
        migrations.AddField(
            model_name="savequeries",
            name="user",
            field=models.OneToOneField(
                default="12:15:23",
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]