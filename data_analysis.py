from data_extraction import extract_data

def analyse_data():
    data = extract_data()
    print(data.describe())
    print(data.info())
    #checking for null values in the dataset
    print(data.isnull().sum())
    #checking for duplicate values in the dataset
    print(data.duplicated().sum())
    print("Features in the data:", data.columns)
    # finding the number of unique values and their occurences
    for column in data.columns:
        counts = data[column].value_counts()
        print(counts)
    return data

analyse_data()
