from datetime import datetime
import threading

import pytz
from rest_framework.response import Response  # Импорты классов
from rest_framework.views import APIView

from .models import PermittedUser, StateUser


# Create your views here.
class UserAccessView(APIView):  # класс который работает с запросами
    lock = threading.Lock()

    @staticmethod
    def get_client_ip(request):  # ф-ция определяющая ip адресс с которого пробросили запрос
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')  # request отвечает за данные с запроса
        if x_forwarded_for:  # мета отвечает за данные в запросе
            ip = x_forwarded_for.split(',')[0].strip()  # разбивает ip адресс по запятой и берёт 1й элемент
        else:  # а также удаляет пробелы до и после строки
            ip = request.META.get('REMOTE_ADDR')
        return ip  # возращает ip адресс из ф-ции

    @staticmethod  # указывает на то, что метод статический (не использует внутри себя self)
    def state_user(request, client_ip):
        # пытаемся получить пользователя по username и hostname
        try:
            return StateUser.objects.get(username=request.data["username"], hostname=request.data["hostname"])
        # если не нашли, то создаём
        except StateUser.DoesNotExist:
            return StateUser.objects.create(
                username=request.data["username"],
                userdomain=request.data["userdomain"],
                hostname=request.data["hostname"],
                ipaddress=request.data["ipaddress"],
                type_of_service=request.data["logontype"],
                localdatetime=datetime.strptime(request.data["localdatetime"], "%Y-%m-%d %H:%M:%S"),
                session_ip=client_ip,
                state="active"
            )

    @staticmethod
    def change_user(user, **kwargs):#Добавил ф-цию которая меняет значения для пользователя валуе
        for key, value in kwargs.items():
            setattr(user, key, value)
        user.save()

    def post(self, request, *args, **kwargs):  # ф-ция Post обрабатывает все входящие post запросы
        client_ip = self.get_client_ip(request)
        type_request = request.data['type'].split()[-1]
        # Получаем тип входа из запроса. Разбиваем по пробелам и берем последний элемент
        # (потому что в последнем элементе лежит ключевое слово)
        if UserAccessView.lock.acquire(blocking=False):
            localdatetime = pytz.timezone('Europe/Moscow').localize(
                datetime.strptime(request.data["localdatetime"], "%Y-%m-%d %H:%M:%S"))
            try:
                PermittedUser.objects.create(  # создаём запись в таблице PermittedUser
                    username=request.data["username"],
                    type_of_log=request.data["type"],
                    userdomain=request.data["userdomain"],
                    hostname=request.data["hostname"],
                    ipaddress=request.data["ipaddress"],
                    type_of_service=request.data["logontype"],
                    localdatetime=localdatetime,
                    session_ip=client_ip,
                )
                if type_request in ['(LOGON)', '(UNLOCK)', '(RECONNECT)']: #укоротил условие
                    self.change_user(
                        self.state_user(request, client_ip),
                        state="active",
                        localdatetime=localdatetime
                    )
                    # Либо получаем такого пользователя, либо создаём
                elif type_request == '(LOGOFF)':
                    self.state_user(request, client_ip).delete()
                    # Получаем такого пользователя и удаляем
                elif type_request == '(LOCK)':
                    self.change_user(
                        self.state_user(request, client_ip),
                        state="locked",
                        localdatetime=localdatetime
                    )
                    # Получаем такого пользователя и меняем state на locked
                elif type_request == '(DISCONNECT)':
                    self.change_user(
                        self.state_user(request, client_ip),
                        state="disconnect",
                        localdatetime=localdatetime
                    )
                    # Получаем такого пользователя и меняем state на disconnect
                elif type_request == '(POWEROFF)':
                    StateUser.objects.filter(
                        hostname=request.data["hostname"],
                        localdatetime__lte=localdatetime#lte меньше или равно
                    ).delete()
                    # Получаем всех пользователей по hostname
                    # localdatetime__lte (время меньше или равно) localdatetime события выключения и удаляем такие записи
            finally:
                UserAccessView.lock.release()
            return Response("Insert done")
