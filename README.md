# Trading Platform Data Puller

This project pulls trading data from various sources and saves it to a CSV file.

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/alexandrasays/trading-platform.git
    cd trading-platform
    ```

2. Create a virtual environment and install dependencies:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. Configure the API URL and headers in `config/config.json`.

## Running the Script

```bash
python scripts/pull_data.py
