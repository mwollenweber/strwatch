# Generated by Django 4.2.16 on 2024-11-30 23:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DataSource",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("url", models.CharField(blank=True, max_length=255, null=True)),
                ("update_interval", models.IntegerField()),
                ("api_key", models.CharField(blank=True, max_length=255, null=True)),
                ("is_active", models.BooleanField(db_index=True, default=False)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("last_modified", models.DateTimeField(auto_now=True)),
                (
                    "last_updated",
                    models.DateTimeField(
                        blank=True,
                        default=datetime.datetime(
                            2023,
                            12,
                            1,
                            23,
                            41,
                            42,
                            283631,
                            tzinfo=datetime.timezone.utc,
                        ),
                        null=True,
                    ),
                ),
                (
                    "last_completed",
                    models.DateTimeField(
                        blank=True,
                        default=datetime.datetime(
                            2023,
                            12,
                            1,
                            23,
                            41,
                            42,
                            284126,
                            tzinfo=datetime.timezone.utc,
                        ),
                        null=True,
                    ),
                ),
                (
                    "last_error",
                    models.DateTimeField(
                        blank=True,
                        default=datetime.datetime(
                            2023,
                            12,
                            1,
                            23,
                            41,
                            42,
                            284143,
                            tzinfo=datetime.timezone.utc,
                        ),
                        null=True,
                    ),
                ),
                ("error_message", models.TextField(blank=True, null=True)),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        db_index=True,
                        default="unknown",
                        max_length=32,
                        null=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Hit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("hit", models.CharField(db_index=True, max_length=255)),
                (
                    "is_new",
                    models.BooleanField(blank=True, db_index=True, default=True),
                ),
                (
                    "is_reviewed",
                    models.BooleanField(blank=True, db_index=True, default=False),
                ),
                (
                    "is_fp",
                    models.BooleanField(blank=True, db_index=True, default=False),
                ),
                (
                    "is_ignored",
                    models.BooleanField(blank=True, db_index=True, default=False),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("last_modified", models.DateTimeField(auto_now=True)),
                ("has_alerted", models.BooleanField(db_index=True, default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Search",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("criteria", models.CharField(max_length=255)),
                ("tolerance", models.IntegerField(blank=True, default=0, null=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "last_updated",
                    models.DateTimeField(
                        blank=True,
                        default=datetime.datetime(
                            2023,
                            12,
                            1,
                            23,
                            41,
                            42,
                            345757,
                            tzinfo=datetime.timezone.utc,
                        ),
                        null=True,
                    ),
                ),
                (
                    "last_ran",
                    models.DateTimeField(
                        blank=True,
                        default=datetime.datetime(
                            2023,
                            12,
                            1,
                            23,
                            41,
                            42,
                            345776,
                            tzinfo=datetime.timezone.utc,
                        ),
                        null=True,
                    ),
                ),
                (
                    "update_interval",
                    models.IntegerField(
                        blank=True, db_index=True, default=1440, null=True
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(blank=True, db_index=True, default=True),
                ),
                (
                    "last_completed",
                    models.DateTimeField(
                        blank=True,
                        default=datetime.datetime(
                            2023,
                            12,
                            1,
                            23,
                            41,
                            42,
                            345799,
                            tzinfo=datetime.timezone.utc,
                        ),
                        null=True,
                    ),
                ),
                (
                    "is_approved",
                    models.BooleanField(blank=True, db_index=True, default=True),
                ),
                (
                    "method",
                    models.CharField(
                        choices=[
                            ("regex", "regex"),
                            ("substring", "substring"),
                            ("strdistance", "strdistance"),
                        ],
                        max_length=20,
                    ),
                ),
            ],
            options={
                "verbose_name": "Search",
                "verbose_name_plural": "Searches",
            },
        ),
    ]
