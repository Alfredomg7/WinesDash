import os
import pandas as pd

def download_data(url):
    df = pd.read_csv(url)
    return df

def prepare_data(df):
    df['Registration Year'] = pd.to_datetime(df['Registration'], errors='coerce').dt.year
    df['Country'] = df['Country'].map({'FR': 'France', 'IT': 'Italy'})
    df['Color'] = df['Color'].str.replace('Rosé', 'Rose')
    selected_columns = ['Country', 'Color', 'Category', 'Registration Year']
    df = df[selected_columns]
    return df

def init_db():
    url = 'https://raw.githubusercontent.com/plotly/Figure-Friday/refs/heads/main/2024/week-46/PDO_wine_data_IT_FR.csv'
    file_path = 'data/prepared_data.csv'

    if not os.path.exists('data'):
        os.makedirs('data')
    if not os.path.exists(file_path):
        print('Downloading data...')
        raw_df = download_data(url)
        print('Preparing data...')
        prepared_df = prepare_data(raw_df)
        prepared_df.to_csv(file_path, index=False)
        print(f'Data prepared and saved to {file_path}.')

if __name__ == '__main__':
    init_db()