import pandas as pd
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random

df=pd.read_csv('medium.csv')
list=df['reading_time'].to_list()

mean=statistics.mean(list)
std=statistics.stdev(list)
print("mean of population distribution: ",mean)
print("standard deviation of population distribution: ",std)
fig = ff.create_distplot([list], ["claps"], show_hist=True)
fig.show()

def random_set_of_means(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(list)-1)
        value=list[random_index]
        dataset.append(value)
    mean_dataset=statistics.mean(dataset)
    mean_std=statistics.stdev(dataset)
    return mean_dataset

def setup():
    mean_list=[]
    for i in range(0,100):
        set_means=random_set_of_means(30)
        mean_list.append(set_means)

    mean=statistics.mean(mean_list)
    stdev=statistics.stdev(mean_list)
    print("mean of sampling distribution: ",mean)
    print("standard deviation of sampling distribution: ",stdev)
    df=mean_list
    fig=ff.create_distplot([df],["Claps"],show_hist=True)
    fig.show()

setup()
