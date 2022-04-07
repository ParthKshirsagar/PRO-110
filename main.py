import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random
import statistics as stats

df = pd.read_csv('medium_data.csv')
data = df['reading_time'].tolist()

pp_mean = stats.mean(data)
pp_std_dev = stats.stdev(data)

print("Population Mean: ", pp_mean)
print("Population Standard Deviation: ", pp_std_dev)

def random_sets_of_mean(counter):
    dataset = []
    for i in (0,counter):
        random_index = random.randint(0,len(data)-1)
        dataset.append(data[random_index])
    mean = stats.mean(dataset)
    return mean

def plot_graph(mean_list):
    fig = ff.create_distplot([mean_list], ['reading_time'], show_hist=False)
    fig.show()

def main():
    mean_list = []
    for i in range(0,100):
        set_of_means = random_sets_of_mean(30)
        mean_list.append(set_of_means)
    plot_graph(mean_list)

    sample_mean = stats.mean(mean_list)
    print("Sample mean: ", sample_mean)
    
main()
