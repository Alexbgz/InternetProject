from base_client import BaseClient
from collections import Counter
import datetime
import requests


class MyClass(BaseClient):  #создаем свой класс на основе базового

    def get_json(user):   #метод выполняющий запрос данных из VK
        bd = (requests.get("https://api.vk.com/method/friends.get?user_id=%s&fields=bdate&v=5.57" % user)).json()
        bd = bd["response"]
        bd = bd["items"]
        return bd    #возвращаем словарь с данными

    def get_age(bd):    #метод определяющий возраст друга
        old=[]
        now = datetime.date.today()
        for bd in bd:
            if bd.get('bdate'):
                date = bd['bdate'].split('.')
                if len(date) == 3:
                    age = now.year - int(date[2])
                    if now.month < int(date[1]):
                        age -= 1
                    elif now.month == int(date[1]) and now.day < int(date[0]):
                        age -= 1
                    old.append(age)
        return old

    def toscreen(old):    #метод составляющий гистограмму возрастов друзей
        d = Counter(old)
        keys = d.keys()
        keys = list(keys)
        keys.sort()
        for i in keys:
            print(i, ':', '#' * d[i])

a = str(input('Введите id: '))
b = MyClass.get_json(a)   #вызываем методы с необходимыми параметрами
c = MyClass.get_age(b)
d = MyClass.toscreen(c)
#23939337


