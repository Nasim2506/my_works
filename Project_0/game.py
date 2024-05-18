import numpy as np
def game_core_v3(number: int= 1) -> int:
    """Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict_number = np.random.randint(1, 101)
    
    #реализуем метод бинарного поиска, введем начальный и конечный диапазоны поиска
    minimum = 0
    maximum = 100
    
    while True:
        count += 1
        # если предсказанное число будет больше загаданного, переопределяем предсказанное число на максимальное в диапазоне и реализуем сужение диапазона поиска 
        if predict_number > number:
            maximum = predict_number - 1
            predict_number = (maximum + minimum ) // 2

        #если предсказанное число будет меньше загаданного, переопределяем предсказанное число на минимальное в диапазоне и реализуем сужение диапазона поиска 
        elif predict_number < number:
            minimum = predict_number + 1
            predict_number = (maximum + minimum ) // 2

        else:
            break  # если загаданное число будет равным предсказанному, выход из цикла

    return count

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score
if __name__ =='__main__':
    print('Run benchmarking for game_core_v3: ', end='')
    score_game(game_core_v3)
