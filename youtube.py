import time # подключение модуля time
class UrTube: # создание класса видеохостинга
    """
    users - список объектов User (list)
    videos - список объектов Video (list)
    current_user - текущий пользователь (User)
    """
    users_dict = {} # пустой сохраняющийся словарь пользователей
    videos_dict = {} # пустой сохраняющийся словарь видео
    users = [] # пустой сохраняющийся список пользователей
    videos = [] # пустой сохраняющийся список видео

    def __init__(self): # инициализация объекта класса UrTube
        self.current_user = 'Нет текущего пользователя'

    def __log_in__(self, nickname, password): # поиск пользователя в списке пользователей
        self.nickname = nickname
        self.password = password
        if self.nickname in self.users and self.users_dict[self.nickname][0] == self.password: # проверка пользователя
            self.current_user = self.nickname # смена текущего пользователя
            print('Выполнен вход в аккаунт: ', self.nickname)
        else:
            print('Неверный логин или пароль')

    def __register__(self, user): # добавление пользователя в список
        self.nickname = user.nickname
        a = isinstance(user.nickname, str)
        b = isinstance(user.password, int)
        c = isinstance(user.age, int)
        if a and b and c: # проверка формата параметров
            self.users_dict[self.nickname] = [user.password, user.age] # добавление пользователя
            self.users = list(self.users_dict.keys()) # формирование списка пользователей
            self.current_user = self.nickname # вход после регистрации
        else:
            print('Неверный формат парметров пользователя')

    def __log_out__(self): # сброс текущего пользователя
        self.current_user = 'Нет текущего пользователя'
        print('Выполнен выход из аккаунта')

    def __add__(self, video): # добавление видео
        self.video = video
        a = isinstance(video.title, str)
        b = isinstance(video.duration, int)
        c = isinstance(video.time_now, int)
        d = isinstance(video.adult_mode, int)
        if a and b and c and d: # проверка формата параметров
            self.videos_dict[video.title] = [video.duration, video.time_now, video.adult_mode] # добавление видео
            self.videos = list(self.videos_dict.keys()) # создание списка видео
        else:
            print('Неверный формат параметров видео')

    def __get_videos__(self, search_word): # поиск видео
        self.search_word = search_word.lower()
        searched_videos = [] # список найденных видео
        for i in self.videos: # цикл перебора списка видео
            if self.search_word in i.lower(): # сверка названий
                searched_videos = searched_videos + [i] # добавление в список найденных
            else:
                continue
        if len(searched_videos) > 0: # проверка на результат поиска
            print('Найденные видео: ', searched_videos)
        else:
            print('Видео не найдено') # сообщение об отрицательных результатах поиска

    def __watch_video__(self, watch_title): # воспроизведение видео
        self.watch_title = watch_title
        if self.current_user == 'Нет текущего пользователя':
            print('Войдите в аккаунт, чтобы посмотреть видео')
        else:
            if self.watch_title in self.videos: # проверка на наличие в списке
                if self.users_dict[self.current_user][1] >= self.videos_dict[watch_title][2]: # проверка на возраст
                    for i in range(self.videos_dict[watch_title][1], self.videos_dict[watch_title][0] + 1): # воспроизведение
                        print(i, ' ', end='') # печать без перехода на следующую строку
                        time.sleep(1) # задержка выполнения
                    print('Конец видео')
                    self.videos_dict[watch_title][1] = 0 # сброс текущего времени просмотра
                else:
                    print('Вам нет', self.videos_dict[self.watch_title][2], 'лет, просмотр запрещён')
            else:
                print('Видео не найдено')

class Video: # создание класса видео
    """
    title - заголовок (str)
    duration - длительность в секундах (int)
    time_now - секунда остановки, изначально 0 (int)
    adult_mode - ограничение по возрасту, по умолчанию False (bool)
    """
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class User: # создание класса пользователей
    """
    nickname - имя пользователя (str)
    password - пароль (int)
    age - возраст (int)
    """
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

# ТЕСТ ----------------------------------------------------------------------------------------------------------------

Oleg = User('Oleg', 123, 50) # создание переменной пользователя Олег
Sasha = User('Alexandra', 321, 15) # создание переменной пользователя Саша
Sveta = User('Svetlana', 49, 456) # создание переменной пользователя Света

Ol_V = Video('Moto', 20, 0, 51) # создание переменной видео Олега
Sa_V = Video('Coffe', 17, 8) # создание переменной видео Саши
Sv_V = Video('Sudak', 25, 0) # создание переменной видео Светы

Tube = UrTube() # создание видеохостинга

Tube.__register__(Oleg) # регистрация пользователя Олег
Tube.__register__(Sasha) # регистрация пользователя Саша
Tube.__register__(Sveta) # регистрация пользователя Света

Tube.__add__(Ol_V) # загрузка видео Олега
Tube.__add__(Sa_V) # загрузка видео Саши
Tube.__add__(Sv_V) # загрузка видео Светы

Tube.__log_in__('Alexandra', 321) # корректный вход в аккаунт Саши
print(Tube.current_user)

Tube.__log_in__('Oleg', 12) # некорректный вход в аккаунт Олега
Tube.__log_in__('Oleg', 123) # корректный вход в аккаунт Олега
Tube.__get_videos__('o') # поиск видео
Tube.__watch_video__('Coffe') # просмотр разрешённого видео
Tube.__watch_video__('Мото') # просмотр отсутствующего видео
Tube.__watch_video__('Moto') # просмотр запрещённого по возрасту видео

print('Словарь пользователей: ', Tube.users_dict)
print('Словарь видео: ', Tube.videos_dict)
print('Список пользователей: ', Tube.users)
print('Список видео: ', Tube.videos)

print(Tube.current_user)
Tube.__log_out__() # выход из аккаунта
print(Tube.current_user)
