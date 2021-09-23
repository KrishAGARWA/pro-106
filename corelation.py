import plotly.express as px
import csv
import numpy as np
def plotfigure(data_path):
    with open(data_path) as csv_file:
        df=  csv_reader=csv.DictReader(csv_file)
        fig=px.scatter(df,x='Marks In Percentage',y='Days Present')
        fig.show()
def getDataSource(data_path):
    marks=[]
    roll=[]
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            marks.append(float(row['Marks In Percentage']))
            roll.append(float(row['Days Present']))
    return{'x':marks,'y':roll
    }    

def findCorelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Temperature vs Ice Cream Sales :- \n--->",correlation[0,1])

def setup():
    data_path ='./data/marks.csv' 
    datasource=getDataSource(data_path)
    findCorelation(datasource)
    plotfigure(data_path)
setup()     
