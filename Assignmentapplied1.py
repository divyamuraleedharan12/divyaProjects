# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 21:28:17 2023

@author: divya
"""

import pandas as pd
import matplotlib.pyplot as plt

"""
The below function is used to create a line chart representing the overall unemployment rate for various countries
Arguments passed inside the function is the dataset for plotting
"""


def lineplot(data1):
    # Line plot data set is stored to a new variable,line_data.
    line_data = data1
    print(line_data)
    # Plot countries with labels
    plt.figure()
    plt.plot(line_data["Year"], line_data["Armenia"], label="Armenia")
    plt.plot(line_data["Year"], line_data["Greece"], label="Greece")
    plt.plot(line_data["Year"], line_data["North Macedonia"], label="North Macedonia")
    plt.plot(line_data["Year"], line_data["Jamaica"], label="Jamaica")
    # Sets the x-axis limit
    plt.xlim(2011, 2021)
    # set x-label for plot axes
    plt.xlabel("Year")
    # set y-label for plot axes
    plt.ylabel("Percentage of total labor force")
    # set title for plot
    plt.title("Unemployment,total(% of total labor force)")
    plt.legend()
    # Saves line plot figure as png
    plt.savefig("Unemployment Lineplot.png")
    # function to show the plot
    plt.show()
    return  # return function is used at the end of a function

""" 
The below function is used to create a bar graph representing the adult mortality rates for different countries in 2018.
Arguments passed inside the function is the dataset for plotting.  
"""


def bargraph(data2):

    # Bar plot data set is stored to a new variable, bar_data.
    bar_data = data2
    print(bar_data)  # prints the dataset
    plt.figure()
    # Bar plot
    plt.bar(bar_data["Country"], bar_data["Mortality rate, adult, male (per 1,000 male adults)"])
    plt.bar(bar_data["Country"], bar_data["Mortality rate, adult, female (per 1,000 female adults)"])
    # Set title for plot
    plt.title("Bar Plot of Mortality Rate in 2018")
    # Set x-label for plot axes
    plt.xlabel("Country")
    # Set y-label for plot axes
    plt.ylabel("Mortality Rate")
    # Saves bar graph figure as png
    plt.savefig("Mortality Rate Bargraph.png")
    # Function to show the plot
    plt.show()
    return

""" 
The function below is used to generate a pie chart showing the prevalence of TB per 100,000 people.
Arguments passed inside the function is the dataset for plotting. 
"""


def piegraph(data3):

    # Pie chart data set is stored to a new variable,pie_data.
    pie_data = data3
    print(pie_data)  # Prints the dataset
    # Creating plot
    plt.figure()
    plt.pie(pie_data["2020"], labels=pie_data["Country"], autopct="%1.1f%%")
    # Set title for plot
    plt.title("Incidence of tuberculosis(per 100,000 people)")
    # Saves pie graph figure as png
    plt.savefig("Prevelance of tuberculosis piegraph.png")
    # Function to show the plot
    plt.show()
    return

if __name__ == "__main__":
    # Reads dataset in excel form for line plot
    data1 = pd.read_excel("unemployment.xlsx")
    # Reads dataset in excel form for bar graph
    data2 = pd.read_excel("mortality_rate.xlsx")
    # Reads dataset in excel form for pie graph
    data3 = pd.read_excel("tuberculosis.xlsx")
    
    # Calling line plot function
    lineplot(data1)
    # Calling bar graph function
    bargraph(data2)   
    # Calling pie graph function
    piegraph(data3)