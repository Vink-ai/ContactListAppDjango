from rest_framework.serializers import ModelSerializer
from .models import Contact

class ContactSerializer(ModelSerializer):

    class Meta:
        model = Contact
        fields = [
            'id',
            'country_code',
            'first_name',
            'last_name',
            'phone_no',
            'contact_pic',
            'is_favorited'
        ]