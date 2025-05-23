from rest_framework import serializers
from .models import Activity


class ActivitySerializer(serializers.ModelSerializer):

    metadata = serializers.DictField(write_only=True)
    timestamp = serializers.DateTimeField(
        format="%Y-%m-%dT%H:%M:%SZ", input_formats=["%Y-%m-%dT%H:%M:%SZ"]
    )

    class Meta:
        model = Activity
        fields = ["event_type", "timestamp", "metadata"]

    def validate_event_type(self, value):
        if value not in ["page_view", "click", "form_submit"]:
            raise serializers.ValidationError(
                "Invalid event type! Please provide event type within event_type field."
            )

    def validate_timestamp(self, value):
        return value

    def create(self, validated_data):
        metadata = validated_data.pop("metadata", {})
        user = self.context["user"]
        return Activity.objects.create(
            user=user,
            page=metadata.get("page", ""),
            browser=metadata.get("browser", ""),
            **validated_data
        )
