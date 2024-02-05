import pandas as pd

def extract_data():
    data = pd.read_csv("segmentation data.csv")
    print(data.head())
    return data

extract_data()
