from pprint import pprint
import requests

class YaUploader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def _get_upload_link(self, file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {'Authorization': '  '}
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload_file_to_disk(self, file_path):
        href = self._get_upload_link(file_path = file_path).get("href", "")
        response = requests.put(href, data=open(file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")

if __name__ == '__main__':
    uploader = YaUploader('Файл.txt')
    result = uploader.upload_file_to_disk('Файл.txt')