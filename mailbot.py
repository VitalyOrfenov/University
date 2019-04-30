import json
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
import datetime
import os


class MailBot:
    price_path = os.path.dirname(
                 os.path.realpath("files\price_list."
                                  "csv")) + "\price_list.csv"
    photo_path = os.path.dirname(
                 os.path.realpath("files\price_list."
                                  "csv")) + "\Russian-Matroshka.png"
    lang_transl_pattern = "https://translate.yandex.net/api" \
                          "/v1.5/tr.json/" \
                          "translate?key=trnsl.1." \
                          "1.20170611T123939Z." \
                          "26dd235c70211" \
                          "8f5.be890c9b0ecb123cac1a78b761" \
                          "fb633b86b0ef90&text={}&lang={}"

    def __init__(self, mail_from, password):
        """Инициализировать объект класса MailBot"""
        self.data_filename = "options.json"
        self.log_filename = "log.txt"
        self._mail_from = mail_from
        self._password = password
        self._clients_data = []
        self._text = ""
        self._msg = None
        self.__server = None

    def __str__(self):
        """Вернуть информацию о версии программы"""
        return "MailBot v2.0"

    def _read_clients(self):
        """Загрузить из файла self.data_filename
           текст письма и информацию о клиентах
        """
        with open(self.data_filename, "r", encoding="utf-8") as fh:
            data = json.loads(fh.read())
        self._text = data["letter"]
        self._clients_data = data["client_info"]

    def _text_translator(self, lang, name):
        """С помощью Yandex API вернуть переведенный
           на язык lang текст письма
        """
        translated_text = requests.get(
                          self.lang_transl_pattern.format(
                              self._text.format(name),
                              lang)).json()["text"][0]
        return translated_text

    def _message_construct(self, client):
        """Создать экземпляр класса MIMEMultipart,
           добавить в него тему, адресанта,
           адресата и текст
        """
        text = self._text_translator(client["lang"], client["name"])
        self._msg = MIMEMultipart()
        self._msg["Subject"] = "Matroshka Offer"
        self._msg["From"] = self._mail_from
        self._msg["To"] = client["email"]
        self._msg.attach(MIMEText(text, "plain"))

    def _message_construct_photo(self):
        """Прикрепить к письму фотографию self.photo_path"""
        with open(self.photo_path, "rb") as image:
            attachment = MIMEImage(image.read())
        attachment.add_header("Content-Disposition",
                              "attachment",
                              filename="Russian-Matroshka.png")
        self._msg.attach(attachment)

    def _message_construct_price(self):
        """Прикрепить к письму файл self.price_path"""
        with open(self.price_path, "rb") as f:
            attachment = MIMEApplication(f.read())
            attachment.add_header("Content-Disposition", "attachment",
                                  filename="price_list.csv")
            self._msg.attach(attachment)

    def _connect_to_serv(self):
        """Подключиться к серверу gmail.com и
           авторизоваться
        """
        self.__server = smtplib.SMTP("smtp.gmail.com", 587)
        self.__server.starttls()
        self.__server.login(self._mail_from, self._password)

    def turn_on_the_bot(self):
        """Запустить программу"""
        self._read_clients()
        self._connect_to_serv()
        with open(self.log_filename, "r+", encoding="utf-8") as fh:
            for client in self._clients_data:
                fh.write("Клиент {} ({})\n".format(client["name"],
                                                   client["email"]))
                self._message_construct(client)
                fh.write("{} - сформировано письмо и "
                         "добавлен текст на языке "
                         "клиента\n".format(datetime.
                                            datetime.now().strftime("%x %X")))
                self._message_construct_photo()
                fh.write("{} - к письму прикреплено"
                         " фото\n".format(datetime.
                                          datetime.now().strftime("%x %X")))
                self._message_construct_price()
                fh.write("{} - к письму прикреплен"
                         " прайс-лист\n".format(datetime.
                                                datetime.
                                                now().strftime("%x %X")))
                self.__server.send_message(self._msg)
                self._msg = None
                fh.write("{} - письмо отправлено\n\n".format(
                    datetime.datetime.now().strftime("%x %X")))
