from data_preprocessing import preprocess_data
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.io as pio
import io
from PIL import Image

def visualize_data():
    data, numerical_columns, categorical_columns = preprocess_data()
    # for numerical_column in numerical_columns:
    #     fig, axs = plt.subplots(figsize=(8,6))
    #     sns.histplot(data, x=numerical_column, kde=True)
    #     plt.show()
    # for categorical_column in categorical_columns:
    #     fig, axs = plt.subplots(figsize=(7,4))
    #     sns.countplot(data=data, x=categorical_column)
    #     plt.show()
    # #comparing gender and (marital status, education)
    # for value in ["marital_status", "education"]:
    #     sns.catplot(data=data, x="sex", col=value, kind="count", height=3, aspect=1.5)
    #     plt.show()
    # #comparing gender, age and maritalstatus
    # sns.barplot(data=data, x="sex", y="age", hue="marital_status")
    # plt.show()
    # #comparing income and gender
    # for value in ["sex", "education", "age", "marital_status"]:
    #     sns.barplot(data=data, x=value, y="income")
    #     plt.show()
    for categorical_feature in categorical_columns:
        fig = px.histogram(data, x=categorical_feature)
        fig.update_layout(template='plotly_dark')
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        # a.append(fig)
        # fig.show()
        fig.write_image(f"histogram_{categorical_feature}.jpg")
    data['sex'] = data['sex'].replace('male', 0)
    data['sex'] = data['sex'].replace('female',1)
    data['marital_status'] = data['marital_status'].replace('single', 0)
    data['marital_status'] = data['marital_status'].replace('non-single', 1)
    data['education'] = data['education'].replace('unknown', 0)
    data['education'] = data['education'].replace('high_school', 1)
    data['education'] = data['education'].replace('university', 2)
    data['education'] = data['education'].replace('graduate', 3)
    data['occupation'] = data['occupation'].replace('unskilled_employee', 0)
    data['occupation'] = data['occupation'].replace('skilled_employee', 1)
    data['occupation'] = data['occupation'].replace('highlyqualified_employee', 2)
    data['settlement_size'] = data['settlement_size'].replace('small_city', 0)
    data['settlement_size'] = data['settlement_size'].replace('midsized_city', 1)
    data['settlement_size'] = data['settlement_size'].replace('big_city', 2)
    #finding outliers 
    # for column in data.columns:
    #     fig, axs = plt.subplots(figsize=(5,4))
    #     sns.boxplot(data[column])
    #     plt.xlabel(column)
    #     plt.show()
    for numerical_feature in data.columns:
        fig = px.box(data, y=numerical_feature)
        fig.update_layout(template='plotly_dark')
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False,zeroline=True,zerolinewidth=4)
        # a.append(fig)
        # fig.show()
        fig.write_image(f"boxplot_{numerical_feature}.jpg")
    return data

visualize_data()
