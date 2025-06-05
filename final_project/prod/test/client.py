import requests

data = {'features':[5.2, 13, 11, 50, 6435, 16, 28, 30, 99, 34, 106, 42, 4.4, 54, 20, 3, 533052, 800, 46, 0.3, 16,
                    84, 987795, 54, 65, 21, 25, 56, 10, 62]}

if __name__ == '__main__':
    # выполняем POST-запрос на сервер по эндпоинту add с параметром json
    r = requests.post('http://localhost:5000/predict', json=data)
    # выводим статус запроса
    print('Status code: {}'.format(r.status_code))
    # реализуем обработку результата
    if r.status_code == 200:
        # если запрос выполнен успешно (код обработки=200),
        # выводим результат на экран
        print('Prediction: {}'.format(r.json()['prediction']))
    else:
        # если запрос завершён с кодом, отличным от 200,
        # выводим содержимое ответа
        print(r.text)