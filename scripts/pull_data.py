import requests
import pandas as pd
import json

def pull_data_from_api(url, headers=None):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return pd.DataFrame(data)
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")

def save_data_to_csv(dataframe, file_path):
    dataframe.to_csv(file_path, index=False)

if __name__ == "__main__":
    api_url = "https://www.alphavantage.co/query?function="
    data = pull_data_from_api(api_url)
    save_data_to_csv(data, "data/trading_data.csv")
