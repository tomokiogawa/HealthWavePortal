from django.db import models
import uuid

class OnCallData(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="id")
    customer_name = models.CharField(verbose_name="利用者氏名")
    start_time = models.DateTimeField(verbose_name="開始時間")
    duration = models.IntegerField(verbose_name="経過時間")
    time_unit = models.CharField(choices={"m" : "分", "s": "秒"}, verbose_name="時間単位")
    content = models.TextField(verbose_name="応対内容")

    def __str__(self):
        return OnCallData.customer_name