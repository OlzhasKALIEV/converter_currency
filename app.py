from flask import Flask, request
import requests

app = Flask(__name__)

API_KEY = "c1e1a06b1a0408683f6b207e38482f20" # Мой ключ


@app.route('/api/rates', methods=['GET'])
def convert_currency():
    from_currency = request.args.get("from")
    to_currency = request.args.get("to")
    value = float(request.args.get("value"))

    url = f"http://apilayer.net/api/live?access_key={API_KEY}&currencies={to_currency}&source={from_currency}&format=1"
    response = requests.get(url)
    data = response.json()

    if 'error' in data:
        return {
            "error": data['error']['info']
        }

    quotes = data.get('quotes')

    if quotes:
        exchange_rate = quotes[f"{from_currency}{to_currency}"]
        converted_value = round(value * exchange_rate, 2)
        result = {
            "result": converted_value
        }
        return result
    else:
        return {
            "error": "Invalid currency"
        }


if __name__ == '__main__':
    app.run(debug=True)
