import requests
from pprint import pprint

class YaUploader:
    def __init__(self, token: str):
        self.token = token
        
    def upload(self, file_path: str):
        """Метод загружает файл file_path на яндекс диск"""
        endpoint = "https://cloud-api.yandex.net:443/"
        put_url = endpoint + "v1/disk/resources/upload"
        param = {"path" : "/123/text.txt", "overwrite": True}
        header = {"Authorization" : self.token}
        resp = requests.get(put_url, params=param, headers=header)
        if resp.status_code != 200:
            return('Что-то пошло не так')
        params = resp.json()
        param2 = params["href"]
        with open(file_path, "rt") as f:
            resp2 = requests.put(param2, files={"file":f})
        if resp2.status_code == 201:
            return 'Файл ' + file_path + ' успешно загружен'
        else:
            return 'Что-то пошло не так'


uploader = YaUploader('')
result = uploader.upload('/home/alex/Документы/text.txt')
print(result)