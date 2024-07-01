import requests
import pandas as pd
import json
from flask import Flask, render_template
import os

app = Flask(__name__)

def load_api_key(file_path):
    with open(file_path, 'r') as file:
        config = json.load(file)
        return config['api_key']

def pull_data_from_alpha_vantage(symbol, api_key):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        time_series = data['Time Series (Daily)']
        df = pd.DataFrame.from_dict(time_series, orient='index', dtype=float)
        df.index = pd.to_datetime(df.index)
        df.sort_index(inplace=True)
        return df
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")

@app.route('/')
def index():
    config_path = "config.json"
    api_key = load_api_key(config_path)
    symbol = "IBM"
    data = pull_data_from_alpha_vantage(symbol, api_key)
    data_html = data.to_html(classes='table table-striped')
    return render_template('index.html', tables=[data_html], titles=[''])

if __name__ == "__main__":
    app.run(debug=True)
