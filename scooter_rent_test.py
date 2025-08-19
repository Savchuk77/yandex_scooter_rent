# Елена Савчук, 33-я когорта, Дипломный проект. Инженер по тестированию плюс

import sender_stand_request


# Функция тестирования создания заказа и получения по треку
def test_scooter_rent():
    # 1. Создание заказа и получение трека
    track_id = sender_stand_request.create_order()
    print(track_id)

    # 2. Получение заказа по его номеру
    res = sender_stand_request.get_order_by_track(track_id)

    # 3. Проверка, что код ответа равен 200.
    assert res.status_code == 200
