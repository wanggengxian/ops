from .serializers import IdcSerializer
from rest_framework import viewsets
from .models import Idc


class IdcViewset(viewsets.ModelViewSet):
    """
    retrieve:
        返回指定IDC信息
    list:
        返回IDC列表
    update:
        更新IDC信息
    destroy:
        删除IDC记录
    create:
        创建IDC记录
    """
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer
