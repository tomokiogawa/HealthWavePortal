from django.db import models
import uuid

class LtcUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="id")


class Logbook(models.Model): # ログブックのデータ
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="id")
    # ログブックのバージョン : 
    # 大項目 : 幼児期、青年期...
    # 中項目 : 質問項目
    # 質問 : 質問文
    # strength, 気になる点  判定
    # メモ