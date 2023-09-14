# converter_currency

команды прописывать в термминале

клонируем репозиторий себе на ПК командой git clone <ссылка на проект>

![img_2.png](img_2.png)

команда: git clone https://github.com/OlzhasKALIEV/converter_currency.git

установка зависимосетей команда: pip install -r .\requirements.txt

запустить сервер python .\app.py run 

рекомендую использовать postman

выполнить запрос GET

GET: http://127.0.0.1:5000/api/rates?from=USD&to=PLN&value=1

![img.png](img.png)

GET: http://127.0.0.1:5000/api/rates?from=USD&to=RUB&value=1

![img_1.png](img_1.png)
