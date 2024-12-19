from datetime import timedelta
from django.forms.models import model_to_dict
from django.contrib.postgres.fields.jsonb import JSONField
from django.utils import timezone
from django.db import models



class STRrecord(models.Model):
    id = models.AutoField(primary_key=True)
    permit_number = models.CharField(blank=True, null=True)
    address = models.CharField(blank=True, null=True)
    permit_type = models.CharField(blank=True, null=True)
    residential_subtype = models.CharField(blank=True, null=True)
    status = models.CharField(blank=True, null=True)
    #expired = models.BooleanField(default=False, blank=True, null=True)
    expired = models.CharField(blank=True, null=True)
    expiration_date = models.DateTimeField(blank=True, null=True)
    bedroom_limit = models.CharField(blank=True, null=True)
    guest_limit = models.CharField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    operator_name = models.CharField(blank=True, null=True)
    operator_phone = models.CharField(blank=True, null=True)
    operator_email = models.CharField(blank=True, null=True)
    operator_permit_number = models.CharField(blank=True, null=True)
    license_holder_name = models.CharField(blank=True, null=True)
    application_date = models.DateTimeField(blank=True, null=True)
    issue_date = models.DateTimeField(blank=True, null=True)
    reference_code = models.CharField(null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True, blank=True)



class Hit(models.Model):
    hit = models.CharField(max_length=255, db_index=True)
    is_new = models.BooleanField(default=True, blank=True, db_index=True)
    is_reviewed = models.BooleanField(default=False, blank=True, db_index=True)
    is_fp = models.BooleanField(default=False, blank=True, db_index=True)
    is_ignored = models.BooleanField(default=False, blank=True, db_index=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    last_modified = models.DateTimeField(auto_now=True, blank=True)
    has_alerted = models.BooleanField(default=False, db_index=True)


class Search(models.Model):
    SEARCH_METHOD_CHOICES = (
        ("regex", "regex"),
        ("substring", "substring"),
        ("strdistance", "strdistance"),
    )
    FIELD_CHOICES = (
        ("any", "any"),
        ("address", "address"),
        ("email", "email"),
        ("name", "name"),
    )

    criteria = models.CharField(max_length=255)
    tolerance = models.IntegerField(default=0, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(
        blank=True, null=True, default=timezone.now() - timedelta(days=365)
    )
    last_ran = models.DateTimeField(
        blank=True, null=True, default=timezone.now() - timedelta(days=365)
    )
    update_interval = models.IntegerField(
        default=1440, blank=True, null=True, db_index=True
    )  # in minutes
    is_active = models.BooleanField(default=True, blank=True, db_index=True)
    last_completed = models.DateTimeField(
        blank=True, null=True, default=timezone.now() - timedelta(days=365)
    )
    is_approved = models.BooleanField(default=True, blank=True, db_index=True)
    method = models.CharField(max_length=20, choices=SEARCH_METHOD_CHOICES)

    class Meta:
        verbose_name = "Search"
        verbose_name_plural = "Searches"
