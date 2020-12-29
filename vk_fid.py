import vk_api
import time

from vk_api.vk_api import VkApiMethod


class VkFid:
    """
    Класс для удобного использования интерфейса авто-отправки рекламного сообщения в группы
    """

    def init(self, token):
        """
        :param token: Токен Страницы вк
        """
        self.token = token
        self.vk = vk_api.VkApi(token=self.token, api_version='5.103')
        self.vk_api: VkApiMethod = self.vk.get_api()
        self.groups = []
        self.time_sleep = 20

    def groups_post(self, text, photo=None):
        """
        Отправляет посты в указанные группы
        :param text: Сообщение - которая будет вылажена в группе
        :param photo: Фотография - которая будет вылажена в группе
        :return:
        """
        success = 0
        for i in self.groups_count():
            group_id = self.groups[i] # id группы
            group_name = self.get_group(group_id)['name'] # имя группы
            try:
                self.vk_api.wall.post(owner_id=group_id, message=text, attachments=photo)
                success += 1
                print("\033[32m ✓\033[37m Пост в группу \033[33m{}\033[37m, был успешно отправлен".format(group_name))
            except:
                print('\033[31m ×\033[37m Вы не учавствуете в группе - \033[33m{}'.format(group_name))
            time.sleep(self.time_sleep)

        print("""
            \033[32m ✓\033[37m Успешно отправленных - \033[33m{}
            \033[31m ×\033[37m Неотправленных - \033[33m{}
            """.format(success, len(self.groups)-success))



    def get_group(self, id_group):
        """
        Выводит информацию группы
        """
        return self.vk_api.groups.getById(group_id=id_group.replace('-', ''))[0]

    def groups_set(self, groups: list):
        """
        Заполнения массива данными из вк групп
        :param groups: Массив с id вк групп
        :return:
        """
        self.groups = groups

    def group_add(self, group):
        """
        Одиночное заполнения массива данными из вк групп
        :param group: id группы вк
        :return:
        """
        self.groups.append(group)

    def groups_count(self):
        """
        Выводит количества вк групп
        :return:
        """
        return range(len(self.groups))

    def timing(self, sec: int):
        self.time_sleep = sec

    def error(self):
        print('error')
        return False