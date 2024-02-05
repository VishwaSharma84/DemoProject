import pandas as pd

def extract_data():
    data = pd.read_csv("https://raw.githubusercontent.com/JyothsnaPendyala/Customer-Segmentation/main/segmentation%20data.csv")
    print(data.head())
    return data

extract_data()
