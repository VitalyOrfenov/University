import requests
import time
import matplotlib.pyplot as plt


class VkFriendsAnalyzer:

    def __init__(self, token):
        """Инициализировать объект класса VkFriendsAnalyzer"""
        assert len(token) > 0, "Токен не может быть пустым"
        if not isinstance(token, str):
            raise TypeError("Ваш персональный токен "
                            "должен быть строкой")
        self.__token = token
        self.filename = "vk_info.txt"

    def __str__(self):
        """Вернуть информацию о версии программы"""
        return "VkFriendsAnalyzer v1.0"

    def _get_list_of_friends(self):
        """Вернуть результат запроса fr_req
           Данный запрос должен вернуть список
           друзей пользователя с указанным именем,
           фамилией, никнеймом и тд. в том порядке,
           в каком друзья расположены на сайте vk.com
        """
        fr_req = "https://api.vk.com/method/{}?order={}&fields={}" \
                 "&access_token={}&v=5.62".format("friends.get",
                                                  "hints",
                                                  "common_count, "
                                                  "nickname",
                                                  self.__token)
        return requests.get(fr_req).json()["response"]

    def _get_list_of_friends_id(self):
        """Вернуть результат запроса fr_id_req
           Данный запрос должен вернуть список
           ID друзей пользователя в том порядке,
           в каком друзья расположены на сайте vk.com
        """
        fr_id_req = "https://api.vk.com/method/{}?order={}" \
                    "&access_token" \
                    "={}&v=5.62".format("friends.get",
                                        "hints",
                                        self.__token)
        return requests.get(fr_id_req).json()["response"]["items"]

    def _get_list_of_friend_schools(self, user_id):
        """Вернуть результат запроса fr_sch_req
           Данный запрос должен вернуть список друзей
           с школами, указанными на их странице vk.com"""
        if not isinstance(user_id, (str, int)):
            raise TypeError("ID пользователя должно быть"
                            "либо числом, либо строкой")
        fr_sch_req = "https://api.vk.com/method/" \
                     "users.get?user_ids={}&" \
                     "fields=schools&" \
                     "access_token={}" \
                     "&v=5.62".format(user_id, self.__token)
        return requests.get(fr_sch_req).json()["response"][0]

    def _get_strings_to_write_1_3(self):
        """Вернуть строку, содержащую информацию
           о количестве друзей. Так же в строке
           содержится имя, никнейм и фамилия каждого друга.
           Так же предоставляется информация о друге, с которым
           у пользователя больше всего общих друзей
        """
        info = self._get_list_of_friends()
        string = "Количество друзей - {}\n".format(str(info["count"]))
        for frnd in info["items"]:
            string += "Имя - {:>10} | Никнейм/Отчество - {:>15} |" \
                      "Фамилия - {:>10}\n".format(frnd["first_name"],
                                                  frnd["nickname"],
                                                  frnd["last_name"])
        string += "\nДруг, с которым больше всего общих друзей:\n"
        most_mut_fr = sorted(info["items"],
                             key=lambda x: x["common_count"],
                             reverse=True)[0]
        string += "Имя - {:>10} | Никнейм/Отчество - {:>15} |" \
                  "Фамилия - {:>10}\n".format(most_mut_fr["first_name"],
                                              most_mut_fr["nickname"],
                                              most_mut_fr["last_name"])
        return string

    def _find_most_pop_fr(self):
        """Вернуть информацию о друге, у которого больше
           всего друзей на странице vk.com
        """
        fr_ids_list = self._get_list_of_friends_id()
        fr_get_pattern = "https://api.vk.com/method/friends.get?" \
                         "user_id={}&access_token={}&v=5.62"
        user_get_pattern = "https://api.vk.com/method/users.get?" \
                           "user_id={}&fields=nickname" \
                           "&access_token={}&v=5.62"
        list_of_fr_dicts = []
        counter = 0
        for uid in fr_ids_list:
            counter += 1
            num_of_fr = requests.get(fr_get_pattern.
                                     format(uid,
                                            self.__token)
                                     ).json()["response"]["count"]
            list_of_fr_dicts.append({"Кол-во друзей": num_of_fr,
                                     "ID": uid})
            if counter % 3 == 0:
                time.sleep(0.9)
        id_most_pop_fr = sorted(list_of_fr_dicts,
                                key=lambda x: x["Кол-во друзей"],
                                reverse=True)[0]["ID"]
        most_pop_fr = requests.get(user_get_pattern.
                                   format(id_most_pop_fr,
                                          self.__token)
                                   ).json()["response"][0]
        return most_pop_fr

    def _get_string_to_write_4(self):
        """Вернуть строку, содержащую информацию
           о друге, у которого больше всего друзей
           на странице vk.com
        """
        most_pop_fr = self._find_most_pop_fr()
        string = "\nСамый популярный друг:\n"
        string += "Имя - {:>10} | Никнейм/Отчество - {:>15} | " \
                  "Фамилия - {:>10}\n".format(most_pop_fr["first_name"],
                                              most_pop_fr["nickname"],
                                              most_pop_fr["last_name"])
        return string

    def _get_info_for_5_6(self):
        """Вернуть словарь, в котором ключи - названия школ,
           а значения - количество друзей пользователя, которые
           в них учились. (Если у друга школа не указана, то
           ведется счет таких же друзей по ключу 'Не указано')
        """
        fr_ids_list = self._get_list_of_friends_id()
        schools_info_pattern = "https://api.vk.com/method/users.get?" \
                               "user_ids={}&fields=schools" \
                               "&access_token={}&v=5.62"
        schools = {}
        counter = 0
        for uid in fr_ids_list:
            counter += 1
            info = requests.get(schools_info_pattern.
                                format(uid, self.__token)
                                ).json()["response"][0]
            if "schools" not in info.keys():
                continue
            else:
                if len(info["schools"]) == 0 and "Не указано" not \
                        in schools.keys():
                    schools["Не указано"] = 1
                elif len(info["schools"]) == 0:
                    schools["Не указано"] += 1
                elif info["schools"][::-1][0]["name"] not in schools.keys():
                    schools[info["schools"][::-1][0]["name"]] = 1
                else:
                    schools[info["schools"][::-1][0]["name"]] += 1
            if counter % 3 == 0:
                time.sleep(0.9)
        return schools

    def _stat_for_bar(self):
        """Создается и настраивается график, основывающийся на
           данных функции _get_info_for_5_6"""
        info = self._get_info_for_5_6()
        fig, ax = plt.subplots()
        fig.canvas.set_window_title("Школы, в которых учились мои друзья")
        ax.set_ylabel("Школы")
        ax.set_xlabel("Количество друзей")
        size = [int(x) for x in info.values()]
        nums = [x + 1 for x in range(len(size))]
        tick_label = [str(x) for x in info.keys()]
        ax.barh(nums, size, tick_label=tick_label, height=0.6, color="green")

    def show_plot(self):
        """Показать график"""
        self._stat_for_bar()
        plt.show()

    def write_text(self):
        """Записать в файл self.filename информацию предоставленную
           функциями _get_strings_to_write_1_3 и
           _get_string_to_write_4
        """
        string = self._get_strings_to_write_1_3()
        string += self._get_string_to_write_4()
        with open(self.filename, "w", encoding="utf-8") as fl:
            fl.write(string)
