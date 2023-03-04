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
    # Line plot data set is stored to a new variable,line_plot.
    line_data = data1
    print(line_data)
    # Plot countries with labels
    plt.figure()
    plt.plot(line_data["Year"], line_data["Armenia"], label="Armenia")
    plt.plot(line_data["Year"], line_data["Greece"], label="Greece")
    plt.plot(line_data["Year"], line_data["North Macedonia"],
             label="North Macedonia")
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

if __name__ == "__main__":
    # Reads dataset in excel form for line plot
    data1 = pd.read_excel("unemployment.xlsx")
    
    # Calling line plot function
    lineplot(data1)
    