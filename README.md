# Заключительный проект "Тестирование автоматизации с Python и Selenium"
## Описание
Этот тестовый скрипт разработан для проверки функционала интернет-магазина товаров.
## Установка и Запуск
1. Клонировать репозиторий с GitHub:
```
https://github.com/Styazhko/finaly_project
```
2. Перейти в директорию проекта.
3. Создать виртуальное окружение:
```
python -m venv venv
```
4. Активировать виртуальное окружение:
```
venv\Scripts\activate
```
5. Установить зависимости:
```
pip install -r requirements.txt
```
6. Запустить автотест (для тестов с маркировкой "need_review", "default='chrome'"):
```
pytest -v --tb=line --language=en -m need_review
```