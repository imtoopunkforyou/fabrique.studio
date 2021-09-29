## fabrique.studio
Test task for www.fabrique.studio

## Задача
Спроектировать и разработать API для системы опросов пользователей.

## Функционал для администратора системы
* Авторизация в системе (регистрация не нужна)
* Добавление/изменение/удаление опросов. Атрибуты опроса: название, дата старта, дата окончания, описание. После создания поле "дата старта" у опроса менять нельзя
* Добавление/изменение/удаление вопросов в опросе. Атрибуты вопросов: текст вопроса, тип вопроса (ответ текстом, ответ с выбором одного варианта, ответ с выбором нескольких вариантов)

## Функционал для пользователей системы
* Получение списка активных опросов
* Прохождение опроса: опросы можно проходить анонимно, в качестве идентификатора пользователя в API передаётся числовой ID, по которому сохраняются ответы пользователя на вопросы; один пользователь может участвовать в любом количестве опросов
* Получение пройденных пользователем опросов с детализацией по ответам (что выбрано) по ID уникальному пользователя

# Установка и запуск

Вы можете использовать виртуальное окружение на вашей машине, если вам так удобнее.

* ``git clone https://github.com/imtoopunkforyou/fabrique.studio.git``
* ``cd ~/strongly-connected``
* ``pip3 install -U pip``
* ``pip3 install -r requirements.txt``
* ``python3 main.py``
