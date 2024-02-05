from data_analysis import analyse_data

def preprocess_data():
    data = analyse_data()
    #renaming the columns in the dataset
    new_column_names = []
    for column_name in data.columns:
        new_column_names.append(column_name.lower().replace(" ", "_"))  
    data.columns = new_column_names
    print(data.head())
    #dropping the column ID
    data.drop(['id'], axis=1, inplace=True)
    numerical_columns = ['age', 'income']
    categorical_columns = ['sex', 'marital_status', 'education', 'occupation', 'settlement_size']
    data['sex'] = data['sex'].replace(0,'male')
    data['sex'] = data['sex'].replace(1,'female')
    data['marital_status'] = data['marital_status'].replace(0, 'single')
    data['marital_status'] = data['marital_status'].replace(1, 'non-single')
    data['education'] = data['education'].replace(0, 'unknown')
    data['education'] = data['education'].replace(1, 'high_school')
    data['education'] = data['education'].replace(2, 'university')
    data['education'] = data['education'].replace(3, 'graduate')
    data['occupation'] = data['occupation'].replace(0, 'unskilled_employee')
    data['occupation'] = data['occupation'].replace(1, 'skilled_employee')
    data['occupation'] = data['occupation'].replace(2, 'highlyqualified_employee')
    data['settlement_size'] = data['settlement_size'].replace(0, 'small_city')
    data['settlement_size'] = data['settlement_size'].replace(1, 'midsized_city')
    data['settlement_size'] = data['settlement_size'].replace(2, 'big_city')
    return data, numerical_columns, categorical_columns

preprocess_data()
