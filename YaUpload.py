token = ''

import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token
        self.headers = {'Authorization': f'OAuth {self.token}'}

    def upload(self, file_path: str):
        """Метод загружает файл на яндекс диск"""
        response = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload',  
                            params={'path': file_path},  
                            headers=self.headers)
        

        print(f'Файл {file_path} успешно загружен на Яндекс.Диск')


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'hero.json'
    token = ''
    uploader = YaUploader(token)
    
