from django.db import models


class PermittedUser(models.Model):
    username = models.CharField(max_length=255, verbose_name="username")
    type_of_log = models.CharField(max_length=255, verbose_name="logon/logoff")
    userdomain = models.CharField(max_length=255, verbose_name="userdomain")
    hostname = models.CharField(max_length=255, verbose_name="hostname")
    ipaddress = models.CharField(max_length=255, verbose_name="ip address")
    type_of_service = models.CharField(max_length=255, verbose_name="Тип Входа в систему")
    time_login = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания записи')


class AlienUser(models.Model):
    username = models.CharField(max_length=255, verbose_name="username")
    type_of_log = models.CharField(max_length=255, verbose_name="logon/logoff")
    userdomain = models.CharField(max_length=255, verbose_name="userdomain")
    hostname = models.CharField(max_length=255, verbose_name="hostname")
    ipaddress = models.CharField(max_length=255, verbose_name="ip address")
    type_of_service = models.CharField(max_length=255, verbose_name="Тип Входа в систему")
    time_login = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания записи')
    session_ip = models.CharField(max_length=255, verbose_name="IP машины с которой пришёл запрос")
