from rest_framework.response import Response  # Импорты классов
from rest_framework.views import APIView

from .models import PermittedUser, AlienUser


# Create your views here.
class UserAccessView(APIView):  # класс который работает с запросами
    @staticmethod
    def get_client_ip(request):  # ф-ция определяющая ip адресс с которого пробросили запрос
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')  # request отвечает за данные с запроса
        if x_forwarded_for:  # мета отвечает за данные в запросе
            ip = x_forwarded_for.split(',')[0].strip()  # разбивает ip адресс по запятой и берёт 1й элемент
        else:  # а также удаляет пробелы до и после строки
            ip = request.META.get('REMOTE_ADDR')
        return ip  # возращает ip адресс из ф-ции

    def post(self, request, *args, **kwargs):  # ф-ция Post обрабатывает все входящие post запросы
        if self.get_client_ip(request) == request.data[
            "ipaddress"]:  # сравнивает с текущим ip c прешедшим с постзапроса
            PermittedUser.objects.create(  # создаём запись в таблице PermittedUser
                username=request.data["username"],
                type_of_log=request.data["type"],
                userdomain=request.data["userdomain"],
                hostname=request.data["hostname"],
                ipaddress=request.data["ipaddress"],
                type_of_service=request.data["logontype"],
            )
            return Response("Insert done")  # возвращяем пользователю сообщение
        AlienUser.objects.create(
            username=request.data["username"],
            type_of_log=request.data["type"],
            userdomain=request.data["userdomain"],
            hostname=request.data["hostname"],
            ipaddress=request.data["ipaddress"],
            type_of_service=request.data["logontype"],
        )
        return Response("Злоумылшенник")  # возвращяем пользователю сообщение