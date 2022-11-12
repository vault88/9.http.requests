import requests
import json
from datetime import datetime, timedelta

# Task 1
heroes_list =  ['Hulk', 'Captain America', 'Thanos']
url = 'https://akabab.github.io/superhero-api/api/all.json'

def most_intelligent_hero(sourse, heroes):
    intelligence_dict = {}
    hero_data = json.loads(requests.get(sourse).content)
    for hero in hero_data:
        if hero['name'] in heroes:
            intelligence_dict[hero['name']] = hero['powerstats']['intelligence']
    return max(intelligence_dict, key=intelligence_dict.get)


if __name__ == '__main__':
    print(f'Самый умный персонаж: {most_intelligent_hero(url,heroes_list)}')


# Task 2
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Get headers
        header = {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}
        # Get upload link
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {'path': file_path, 'overwrite': True}
        response = requests.get(url, headers=header, params=params)
        upload_url = response.json()['href']
        try:
            response = requests.put(upload_url, data=open(file_path, 'rb'), headers=header)
        except FileNotFoundError:
            print(f'Файл {file_path} не найден!')
        if response.status_code == 201:
            print(f'Файл {file_path} успешно загружен на ЯндексДиск')
        else:
            print(f'Файл {file_path} не удалось загрузить')


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'file.md'
    token = ...
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)

# Task 3

def stack_data(tags,days=2):
    todate = datetime.now()
    fromdate = todate - timedelta(days=2)
    url = 'https://api.stackexchange.com/'
    uri = f'/2.3/questions?fromdate={int(fromdate.timestamp())}&todate={int(todate.timestamp())}&order=desc&sort=activity&tagged={tags}&site=stackoverflow'
    response = requests.get(url + uri)
    response_list = response.json()['items']# result =  ['items']
    for element in response_list:
        print(element['title'])

if __name__ == '__main__':
    stack_data('Python')
