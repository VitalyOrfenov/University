import re
import requests


class BookInfoCollector:
    """Класс BookInfoCollector реализует поиск информации
       при помощи регулярных выражений

       *_REGEX - константы класса, содержащие регулярные выражения
       для нахождения нужных строк

       REGEX_TUPLE - кортеж констант
    """
    NAME_REGEX = r"<h1>(.+)<\/h1>"
    AUTHORS_REGEX = r"<h2><a href=.+>(.+)<\/a><\/h2>"
    COST_REGEX = r"<div class=.price.><span  >(\d+)?<\/span>"
    ISBN_REGEX = r"ISBN: <\/span>(.+)<\/p>"
    PUB_REGEX = r"<a href=\"\/\w+\/.+\('producer'\);\">(.+?)<\/a>"
    PAGE_REGEX = r"Количество страниц: <\/span>(.+)<\/p>"
    YEAR_REGEX = r"<a href=\"\/\w+\/.+\/\".+\(\'producer'\);\">.+>(.+)<\/a>"
    REGEX_TUPLE = (NAME_REGEX, AUTHORS_REGEX, COST_REGEX, ISBN_REGEX,
                   PUB_REGEX, PAGE_REGEX, YEAR_REGEX)

    def __init__(self, html_adress, result_filename):
        """Инициализация класса """
        self.html_adr = html_adress
        self.html_filename = "data.html"
        self.res_filename = result_filename
        self.data = None

    def __str__(self):
        """Строковое представление класса """
        return "Поиск информации о книге v1.0"

    def _load_html(self):
        """Загрузка html-страницы"""
        r = requests.get(self.html_adr)
        data = r.text
        if r.status_code == requests.codes.ok:
            with open(self.html_filename, "w", encoding="utf-8") as fl:
                fl.write(data)
        else:
            raise (requests.HTTPError, requests.ConnectionError)

    def _html_read(self):
        """Прочитать сохраненный html-файл и
           присвоить его содержимое переменной self.data
        """
        self._load_html()
        with open(self.html_filename, "r", encoding="utf-8") as fh:
            html = fh.read()
            html = html.replace("&nbsp;", " ")
            self.data = html
            print("Перенос html-кода завершен")

    def _match_seeker(self):
        """Искать совпадения в self.data по каждому регулярному выражению
           в REGEX_TUPLE, добавить в match_list и вернуть список
           строк, которые были найдены по регулярным выражениям"""
        self._html_read()
        match_list = []
        for patt in self.REGEX_TUPLE:
            match_list.append(*re.findall(patt, self.data))
        return match_list

    def load(self):
        """Записать в файл найденые с помощью регулярных выражений строки"""
        data = self._match_seeker()
        with open(self.res_filename, "w", encoding="UTF-8") as fl:
            string = "Название - {}\n" \
                     "Автор - {}\n" \
                     "Цена (руб.) - {}\n" \
                     "ISBN - {}\n" \
                     "Издательство - {}\n" \
                     "Количество страниц - {}\n" \
                     "Год издания - {}".format(*data)
            print(string)
            fl.write(string)
