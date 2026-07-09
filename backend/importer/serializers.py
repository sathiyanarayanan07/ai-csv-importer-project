from rest_framework import serializers
from .models import Upload,CRMLead

class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upload
        fields = ["id","file","uploaded_at",]
        read_only_fields = ["id","uploaded_at"]


class CRMLeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = CRMLead
        fields = [
            "id",
            "upload",
            "created_at",
            "name",
            "email",
            "country_code",
            "mobile_without_country_code",
            "company",
            "city",
            "state",
            "country",
            "lead_owner",
            "crm_status",
            "crm_note",
            "data_source",
            "possession_time",
            "description",
            "imported_at",
        ]
        read_only_fields = ["id", "imported_at"]