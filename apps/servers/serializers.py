from rest_framework import serializers
from .models import Server, NetworkDevice, IP
from .models import Manufacturer, ProductModel


class ServerAutoReportSerializer(serializers.Serializer):
    """
    服务器同步序列化类
    """
    ip = serializers.IPAddressField(required=True)
    hostname = serializers.CharField(required=True, max_length=20)
    cpu = serializers.CharField(required=True, max_length=50)
    mem = serializers.CharField(required=True, max_length=20)
    disk = serializers.CharField(required=True, max_length=200)
    os = serializers.CharField(required=True, max_length=50)
    sn = serializers.CharField(required=True, max_length=50)
    manufacturer = serializers.CharField(required=True)
    model_name = serializers.CharField(required=True)
    uuid = serializers.CharField(required=True, max_length=50)
    network = serializers.JSONField(required=True)

    def validate_manufacturer(self, value):
        try:
            return Manufacturer.objects.get(vendor_name__exact=value)
        except Manufacturer.DoesNotExist:
            return self.create_manufacturer(value)

    def create_manufacturer(self, vendor_name):
        return Manufacturer.objects.create(vendor_name=vendor_name)

    def validate(self, attrs):
        manufacturer_obj = attrs["manufacturer"]
        try:
            attrs["model_name"] = manufacturer_obj.productmodel_set.get(
                model_name__exact=attrs["model_name"])
        except ProductModel.DoesNotExist:
            attrs["model_name"] = self.create_product_model(
                manufacturer_obj, attrs["model_name"])
        return attrs

    def create_product_model(self, manufacturer_obj, model_name):
        return ProductModel.objects.create(model_name=model_name, vendor=manufacturer_obj)

    def create(self, validated_data):
        print(validated_data)
        pass


class ServerSerializer(serializers.ModelSerializer):
    """
    服务器序列化类
    """
    class Meta:
        model = Server
        fields = "__all__"


class NetworkDeviceSerializer(serializers.ModelSerializer):
    """
    网卡序列化
    """
    class Meta:
        model = NetworkDevice
        fields = "__all__"


class IPSerializer(serializers.ModelSerializer):
    """
    IP序列化
    """
    class Meta:
        model = IP
        fields = "__all__"
