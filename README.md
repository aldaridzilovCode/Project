Инструкция запуска

Создание виртуального окружения:

py -m venv .venv (после установки файлов, программа должна автоматически зайти в область pythonа, но если не зашло то .venv\Scripts\Activate.ps1)

Установка зависимостей:

pip install -r requirements.txt

Загрузка данных:

python downloader.py

Расчёт индикаторов:

python indicators.py

Запуск интерфейса:

streamlit run app.py