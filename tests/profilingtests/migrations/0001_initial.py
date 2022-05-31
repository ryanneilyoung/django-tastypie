# Generated by Django 2.2.1 on 2019-05-28 22:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tastypie.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Note",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("slug", models.SlugField()),
                ("content", models.TextField(blank=True)),
                ("is_active", models.BooleanField(default=True)),
                ("created", models.DateTimeField(default=tastypie.utils.timezone.now)),
                ("updated", models.DateTimeField(default=tastypie.utils.timezone.now)),
                (
                    "author",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
