import configuration
import data

# Импорт библиотеки requests для выполнения HTTP-запросов
import requests

# Функция создания заказа


def create_order():
    res = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                        json=data.order_body,
                        headers=data.headers)
    json = res.json()
    return json.get('track')

# Функция получения заказа по его номеру


def get_order_by_track(track_id):
    path = configuration.URL_SERVICE + \
        configuration.GET_ORDER_BY_TRACK_PATH + str(track_id)
    print(path)
    return requests.get(path, data.headers)

# Функция тестирования создания заказа и получения по треку


def test_scooter_rent():
    # 1. Создание заказа и получение трека
    track_id = create_order()
    print(track_id)

    # 2. Получение заказа по его номеру
    res = get_order_by_track(track_id)

    # 3. Проверка, что код ответа равен 200.
    assert res.status_code == 200
