import random
import datetime


class GuessTheNumber:
    """Класс GuessTheNumber имитирует ход игры
       'Угадай число'
    """
    def __init__(self):
        """Инициализирует класс GuessTheNumber"""
        self.time_of_begin = datetime.datetime.now().strftime("%x %X")
        self.game_status = True
        self.number_of_atts = 0
        self.play_interval = None
        self.time_of_end = 0
        self.filename = "gameinfo.txt"

    def __str__(self):
        """Строковое представление класса GuessTheNumber"""
        return "Игра 'Угадай число'"

    def get_a_interval(self, beg, end):
        """self.play_interval - начало и конец интервала, внутри
           которого заключено загаданное число
        """
        if not isinstance(beg, int) and not isinstance(end, int):
            raise ValueError("Начало и конец интервала "
                             "должны быть целыми числами")
        self.play_interval = [beg, end]

    def try_a_number(self):
        """Возвращает число, сгенерированное случайным образом
           в границах интервала self.play_interval"""
        number = random.randint(*self.play_interval)
        return number

    def check_a_number(self, answer, number):
        """Проверяет действительно ли сгенерированное число
           соответсвует загаданному, если нет, то вызывается
           функция, которая изменяет границы интервала, если
           же соответствует, то фиксируется время окончания игры
        """
        assert isinstance(number, int), "Предполагаемое число должно" \
                                        "быть целым "
        if not isinstance(answer, int):
            raise ValueError("Ответ на вопрос должен быть целым числом")
        if answer == 1:
            self.number_of_atts += 1
            self.game_status = False
            self.time_of_end = datetime.datetime.now().strftime("%x %X")
            return "Я угадал твое число! Это число - {}".format(number)
        elif answer == 0:
            self.number_of_atts += 1
            self.change_interval(number)

    def change_interval(self, tried_num):
        """Изменяет границы интервала self.play_interval
           в зависимости от указания, больше tried_num
           задуманного числа или нет
        """
        assert isinstance(tried_num, int), \
            "Предполагаемое число должно" \
            "быть целым "
        comp = input("Загаданное число больше или меньше {}?"
                     "(> - больше, < - меньше): ".format(tried_num))
        if comp == ">" and tried_num == self.play_interval[1]:
            raise ValueError("Нарушение границ интервала")
        elif comp == "<" and tried_num == self.play_interval[0]:
            raise ValueError("Нарушение границ интервала")
        elif comp == ">":
            self.get_a_interval(tried_num+1, self.play_interval[1])
        elif comp == "<":
            self.get_a_interval(self.play_interval[0], tried_num-1)

    def save(self):
        """Сохраняет итог игры в self.filename"""
        with open(self.filename, "r+", encoding="UTF-8") as fh:
            fh.write("Игра №{}\n".format((len(fh.readlines())//5 + 1)))
            fh.write("Время начала игры - "
                     "{}\n".format(self.time_of_begin))
            fh.write("Время конца игры - "
                     "{}\n".format(self.time_of_end))
            fh.write("Количество затраченных попыток - "
                     "{}\n\n".format(self.number_of_atts))
