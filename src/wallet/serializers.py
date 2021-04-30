from rest_framework import serializers

from wallet.models import Wallet
from user.serializers import UserLiteSerializer


class WalletSerializer(serializers.ModelSerializer):
    user_details = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Wallet
        fields = '__all__'

    def get_user_details(self, obj: Wallet):
        return UserLiteSerializer(obj.user).data
