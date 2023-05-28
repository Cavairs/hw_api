import requests
from pprint import pprint
import json
import os

if not os.path.exists("upload"):
    os.mkdir("upload")


class YaUploader:  # класс
    def __init__(self, token: str):
        self.token = token
        self.headers = {'Content-Type': 'application/json',
                        'Authorization': f'OAuth {self.token}'}

    # Получаем файл с списком файлов на диске

    def get_files_list(self):  # метод класса
        # ссылка для выполнения гет запроса
        method_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        # в параметрах указываем путь до диска в нашем случаи это корневой каталог /
        params = {'path': '/'}
        # гет запрос , получаем мета данные о файлах на диске
        response = requests.get(
            method_url, headers=self.headers, params=params)
        # сохраняем ответ в переменную в формате json
        data = response.json()
        files_name = []  # Пустиой список для получения имени файлов по ключу name
        for name_file in data['items']:  # для перменной name_file в словаре data по ключу items  делаем перебор и дабавляем в сисок значения с ключем name
            # дабавляем в сисок значения с ключем name
            files_name.append(name_file["name"])
        pprint(files_name)
        # открываем или создаем если нет файл my_files_in_my_disk.txt в который принимаем список из имени файлов на диске
        with open('upload/my_files_in_my_disk.txt', 'w+', encoding='utf-8') as f:
            # объеденяем спиок в одну строку
            f.write('\n'.join(files_name))
        return files_name  # возврат метода

    # Создание папки. \n path: Путь к создаваемой папке.
    def create_folder(self):
        method_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {
            'path': r'upload'
        }
        requests.put(method_url, params=params, headers=self.headers)

    def _get_upload_link(self, disk_file_path):
        method_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(
            method_url, headers=self.headers, params=params)
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        href = self._get_upload_link(
            disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Файл загружен на диск")


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    token = ''
    # сказали что ya_uploader это эксемпляр класса YaUploader
    ya_uploader = YaUploader(token)
    # запуск  метода у объекта ya_uploader (он же экземпляр класса YaUploader он создает txt файл в папке upload с списком файлов на в локальной дериктории)
    ya_uploader.get_files_list()
    ya_uploader.create_folder()
    ya_uploader.upload_file_to_disk(
        'upload/my_files_in_my_disk.txt', 'upload/my_files_in_my_disk.txt')
