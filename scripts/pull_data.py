import requests
import pandas as pd
import json

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

def save_data_to_csv(dataframe, file_path):
    dataframe.to_csv(file_path, index=True)

if __name__ == "__main__":
    api_key = "YOUR_API_KEY"
    symbol = "IBM"
    data = pull_data_from_alpha_vantage(symbol, api_key)
    save_data_to_csv(data, "data/ibm_daily.csv")
