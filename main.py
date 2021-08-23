"""
Written by Martin Karlsson
www.martinkarlsson.io

Install requirements before executing the code:
python3 -m pip install -r requirements.txt

Purpose for this tutorial is to show how to easily utilize a Robust Random Cut Forest neural network to find anomalies in time series data.
It will utilize multiprocessing to efficiently run multiple RCCF processes in parallell. This will decrease the execution time.
"""

import numpy as np
import pandas as pd
import rrcf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import random
import datetime
from multiprocessing import Process, Pipe
import multiprocessing

#Set tree parameters for Robust Random Cut Forest
num_trees = 40
shingle_size = 15
tree_size = 256

#Path to the dataset
datasetPath = 'data/example-dataset.csv'

def anomalyRate(data,anomaly):
    dataLen = int(len(data))
    #Create a forest of empty trees
    forest = []
    for _ in range(num_trees):
        tree = rrcf.RCTree()
        forest.append(tree)
        
    #Creating a rolling window(shingle_size) by using the built in shingle generator
    points = rrcf.shingle(data, size=shingle_size)

    #Create a dict to store anomaly score of each point
    avg_codisp = {}

    #For each shingle...
    for index, point in enumerate(points):
        #For each tree in the forest...
        for tree in forest:
            #If tree is above permitted size, drop the oldest point (FIFO)
            if len(tree.leaves) > tree_size:
                tree.forget_point(index - tree_size)
            #Insert the new point into the tree
            tree.insert_point(point, index=index)
            #Compute codisp on the new point and take the average among all trees
            if not index in avg_codisp:
                avg_codisp[index] = 0
            avg_codisp[index] += tree.codisp(index) / num_trees
    #Create a list with anomaly ratings
    for counter in range(0,dataLen-shingle_size):
        anomaly.append(round(float(avg_codisp[counter]),2))
    #Fills out with 0's for the time smaller than the shingle_size(was not rated), this to have a consistent length on the list
    for counter in range (len(anomaly),dataLen):
        anomaly.append(0)

def __main__():
    dataframe = pd.read_csv(datasetPath)
    epochs = dataframe['epoch'].tolist()
    #Get all the columns in the dataframe
    dataTitles = dataframe.keys()
    dataTitles = dataTitles.tolist() #Makes a list of it
    dataTitles.remove('epoch') #Remove epoch from the list

    #Generate a dict with all the data in list format
    dataDict = {}
    for dataTitle in dataTitles:
        dataDict[dataTitle] = dataframe[dataTitle].tolist()

    #Using Multiprocessing Manager we declare lists that will be returned from each process
    manager = multiprocessing.Manager()
    data1Anomaly = manager.list()
    data2Anomaly = manager.list()
    data3Anomaly = manager.list()
    data4Anomaly = manager.list()
    data5Anomaly = manager.list()
    data6Anomaly = manager.list()
    data7Anomaly = manager.list()
    data8Anomaly = manager.list()
    data9Anomaly = manager.list()
    data10Anomaly = manager.list()
    data11Anomaly = manager.list()
    data12Anomaly = manager.list()

    #Creates all the processes
    processes = []
    process = Process(target=anomalyRate, args=(dataDict['data1'],data1Anomaly,))
    processes.append(process)
    process = Process(target=anomalyRate, args=(dataDict['data2'],data2Anomaly,))
    processes.append(process)
    process = Process(target=anomalyRate, args=(dataDict['data3'],data3Anomaly,))
    processes.append(process)
    process = Process(target=anomalyRate, args=(dataDict['data4'],data4Anomaly,))
    processes.append(process)
    process = Process(target=anomalyRate, args=(dataDict['data5'],data5Anomaly,))
    processes.append(process)
    process = Process(target=anomalyRate, args=(dataDict['data6'],data6Anomaly,))
    processes.append(process)
    process = Process(target=anomalyRate, args=(dataDict['data7'],data7Anomaly,))
    processes.append(process)
    process = Process(target=anomalyRate, args=(dataDict['data8'],data8Anomaly,))
    processes.append(process)
    process = Process(target=anomalyRate, args=(dataDict['data9'],data9Anomaly,))
    processes.append(process)
    process = Process(target=anomalyRate, args=(dataDict['data10'],data10Anomaly,))
    processes.append(process)
    process = Process(target=anomalyRate, args=(dataDict['data11'],data11Anomaly,))
    processes.append(process)
    process = Process(target=anomalyRate, args=(dataDict['data12'],data12Anomaly,))
    processes.append(process)
    
    #Start all the processes
    startProcessesCounter = 0
    processesLen = len(processes)
    while startProcessesCounter < processesLen:
        processes[startProcessesCounter].start()
        startProcessesCounter += 1

    #Make sure all processes has finished
    for process in processes:
        process.join()

    #Initiate the plot area
    fig, axs = plt.subplots(2,1,figsize=(16,9), gridspec_kw={'height_ratios': [4, 1]})
    axs[0].xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M')) #Set to show date
    timestamps = []

    #Convert epoch to date
    for epoch in epochs:
        timestamps.append(datetime.datetime.utcfromtimestamp(epoch))

    #Create a couple of colors to use
    usedColors = []
    colors = ['forestgreen','teal','indigo','khaki','palegreen','crimson','coral','tan','peru','tab:orange','tab:green','tab:purple','tab:brown','tab:pink','tab:gray','tab:olive','tab:cyan']

    for data in dataTitles:
        #Generate a unique color
        randInt = random.randint(0, len(colors)-1)
        color = colors[randInt]
        while color in usedColors:
            randInt = random.randint(0, len(colors)-1)
            color = colors[randInt]
            if len(usedColors) == len(colors):
                usedColors = []
        usedColors.append(color)
        #Plot the data
        axs[0].plot(timestamps,dataDict[data],linewidth=1,color=color)

    #Creates a list with the average anomaly rating for all dataseries
    anomalyCombined = []
    for n in range(0,len(epochs)):
        anomalyCombined.append((data1Anomaly[n]+data2Anomaly[n]+data3Anomaly[n]+data4Anomaly[n]+data5Anomaly[n]+data6Anomaly[n]+data7Anomaly[n]+data8Anomaly[n]+data9Anomaly[n]+data10Anomaly[n]+data11Anomaly[n]+data12Anomaly[n])/12)

    #Plotting the anomaly rating in the second plot area
    axs[1].plot(timestamps,anomalyCombined,linewidth=1,color="red")
    plt.show()

__main__()