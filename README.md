Инструкция запуска

Создание виртуального окружения:

python -m venv .venv
(если не зашло то .venv\Scripts\Activate.ps1)

Установка зависимостей:

pip install -r requirements.txt

Загрузка данных:

python downloader.py

Расчёт индикаторов:

python indicators.py

Запуск интерфейса:

streamlit run app.py