import requests

BATCH_SIZE = 1000 # рандомное количество объектов, которые мы хотим выгрузить за один запрос
HOST = 'localhost'# рандомное имя для псевдокода
PORT = 8080 # рандомный порт
# Устанавливаем базовый URL для запросов к API
BASE_URL = "http://${HOST}:${PORT}"
Q = "(core.resourceType:Oracle or core.resourceType:PowerCenter)"
cursor = "*"
sortField="id%20asc" 
OBJECT_PATH = "/access/1/catalog/data/objects?q=${Q}&cursorMark=${cursor}&sort=${sortField}&pageSize=20" # путь взять из прмера
#параметры для первого запроса
params = {
    "offset": 0,
    "limit": BATCH_SIZE
}
#функция для обработки данных, для псевдокода пусть будет принт
def process_data(data):
    print(data)
#первый запрос
response = requests.get(BASE_URL + OBJECT_PATH, params=params)
#ответ
while response.status_code == 200:
    process_data(response.json())
    # Если мы получили меньше объектов, чем запросили, значит, это был последний запрос
    if len(response.json()["items"]) < BATCH_SIZE:
        break
    #параметры для следующего запроса
    params["offset"] += BATCH_SIZE
    #следующий запрос
    response = requests.get(BASE_URL + OBJECT_PATH, params=params)