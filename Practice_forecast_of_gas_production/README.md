# Практика. Линейная алгебра в контексте линейных методов
У Василия, основателя компании «Газ-Таз-Ваз-Нефть», дела идут в гору: у него уже функционирует 200 скважин для добычи газа. В этом году он открывает 30 новых скважин. Однако в целях оптимизации расходов и повышения дохода Василию необходимо оценить, сколько денег будет приносить ему каждая из скважин, а также понять, какие факторы (параметры скважин) потенциально сильнее всего повлияют на объём добычи газа.

Для этого Василий решил нанять вас как специалиста в области Data Science.

Задача — построить регрессионную модель, которая прогнозирует выработку газа на скважине (целевой признак — Prod) на основе остальных характеристик скважины, и проинтерпретировать результаты работы вашей модели.

Цели проекта:

- Построение линейной регрессии по методу наименьших квадратов с помощью библиотеки numpy.
- улучшить результат — уменьшить ошибку прогноза с помощью модели полиномиальной регрессии.
- Применение L1, L2-регуляризаций, используя кросс-валидацию.

Основные этапы работы с данными:

Разделим эту задачу на две части:

1. В первой мы построим простейшую модель линейной регрессии, проанализируем результаты её работы и выберем наиболее значимые для прогнозирования факторы.

2. Во второй мы займёмся построением модели полиномиальной регрессии с регуляризацией и посмотрим на итоговые результаты моделирования.

## Описание данных 

Василий предоставляет нам набор данных о добыче газа на своих скважинах.

- Well — идентификатор скважины;
- Por — пористость скважины (%);
- Perm — проницаемость скважины;
- AI — акустический импеданс ($кг/м^2 * 10^6$);
- Brittle — коэффициент хрупкости скважины (%);
- TOC — общий органический углерод (%);
- VR — коэффициент отражения витринита (%);
- Prod — добыча газа в сутки (млн. кубических футов).

  ## Выводы

  ***В результате избавлениния от сильно-коррелирующих между собой признаков, последующего масштабирования и возведения в степень полинома признаков, оказалась наиболее удачной модель линейной регрессии с регуляризацией L1 (Lasso -регуляризация), которая показала адекватные показатели средней абсолютной ошибки в процентах (MAPE), а также уменьшившую переобученность модели***
