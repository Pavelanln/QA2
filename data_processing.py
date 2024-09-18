# Data processing script
import pandas as pd

def process_data(file_path):
    data = pd.read_csv(file_path)
    summary = data.describe()
    print('Data Summary:', summary)
    
if __name__ == '__main__':
    process_data('data.csv')
