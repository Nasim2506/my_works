# Практика: Подбор гиперпараметров модели на примере Kaggle: Predicting a Biological Response

## Оглавление
[1. Описание проекта](https://github.com/Nasim2506/my_works/edit/master/practice_optimization_hyperparameters/README.mdОписание-проекта)

[2. Какой кейс решаем?](https://github.com/Nasim2506/my_works/edit/master/practice_optimization_hyperparameters/README.mdКакой-кейс-решаем)  

[3. Краткая информация о данных](https://github.com/Nasim2506/my_works/edit/master/practice_optimization_hyperparameters/README.mdКраткая-информация-о-данных)  

[4. Этапы работы над проектом](https://github.com/Nasim2506/my_works/edit/master/practice_optimization_hyperparameters/README.md#Этапы-работы-над-проектом)  

[5. Результат](https://github.com/Nasim2506/my_works/edit/master/practice_optimization_hyperparameters/README.md#Результат)    

[6. Выводы](https://github.com/Nasim2506/my_works/edit/master/practice_optimization_hyperparameters/README.md#Выводы) 

### Описание проекта  
Построение модели с дальнейшей оптимизацией гиперпараметров

:arrow_up:[к оглавлению](https://github.com/Nasim2506/my_works/edit/master/practice_optimization_hyperparameters/README.md#Оглавление)

### Какой кейс решаем?    

Построить базовые модели(Baseline) - логистическую регрессию(LogisticRegression) и случайный лес(RandomForestClassifier). Подобрать оптимальные гиперпараметры моделей четырмя методами: GridSeachCV, RandomizedSearchCV, Hyperopt, Optuna. За основу взять Kaggle: Predicting a Biological Response.

**Условия соревнования**

Решение оформляется только в Jupyter Notebook
Каждое задание выполняется в отдельной ячейке, выделенной под задание. Не следует создавать множество ячеек для решения задачи
Код для каждого задания оформляется в одной-двух jupyter-ячейках (не стоит создавать множество ячеек для решения задачи).
Решение должно использовать только: переменные, основные структуры данных (списки, словари, множества), циклы, функции, библиотеки numpy, pandas, matplotlib, seaborn, plotly.
Код должен быть читаемым и понятным: имена переменных и функций отражают их сущность, важно избегать многострочных конструкций и условий. Код оформлен согласно руководству PEP 8.
Графики должны содержать название, отражающее их суть, и подписи осей.
Выводы к графикам оформляются в формате Markdown под самим графиком в отдельной ячейке. Выводы должны быть представлены в виде небольших связанных предложений на русском языке.

**Метрика качества**

- Решение оформлено согласно требованиям "Условия соревнования"
- Соблюдены и выполнены все этапы проекта с заданиями, представлены выводы и графики
- Результаты оцениваются по метрике F1
- Гиперпараметры подобраны четырьмя методами
- Решение размещено на Git hub

**Что практикуем**

Учимся писать хороший код на Python, практикуем: написание функций, умения выбирать и применять статистические тесты, проверять гипотезы, базовые/продвинутые методы работы с данными в Pandas, визуализацию, моделирование, подбор гиперпараметров, работа с документацией

:arrow_up:[к оглавлению](https://github.com/Nasim2506/my_works/edit/master/practice_optimization_hyperparameters/README.md#Оглавление)

### Краткая информация о данных

**Для работы были использованы данные:**

Набор данных для прогнозирование биологического ответа(train_sem09__1.zip) 

:arrow_up:[к оглавлению](https://github.com/Nasim2506/my_works/edit/master/practice_optimization_hyperparameters/README.md#Оглавление)

### Этапы работы над проектом

- Базовый анализ структуры данных, преобразование данных
- Построение базовых моделей
- Моделирование и подбор гиперпараметров
- Итоги 

:arrow_up:[к оглавлению](https://github.com/Nasim2506/my_works/edit/master/practice_optimization_hyperparameters/README.md#Оглавление)

### Результаты

Получены метрики моделей при оптимальных гиперпараметрах, подобранные различными методами, проведено сравнение методов, сделаны выводы.

:arrow_up:[к оглавлению](https://github.com/Nasim2506/my_works/edit/master/Project_1/Readme.md#Оглавление)

### Выводы

Задачи проекта выполнены полностью с соблюдением всех этапов. Выводы сделаны в работе
:arrow_up:[к оглавлению](https://github.com/Nasim2506/my_works/edit/master/practice_optimization_hyperparameters/README.md#Оглавление)
