"""
                         +================+
                        ||  Challenge 8  ||
                        +================+
Dataframes have something called an index. Because we didn't specify what the
index column was when loading the data, pandas automatically assigns a number
index from 0, 1, 2, ..., etc.

When we did df.max(), notice that it showed us the maximum datetime too. Let's
instead make the index be our time stamps.

1) Use the dataframe object method set_index() to make the timestamps the index

2) find the maximum values again. Notice how the datetime output should have
    vanished.

3) extract only the power values into a new variable called data.

4) using matplotlib, plot a histogram of the power data.
    - try using the kwarg bins=100
    - now add another kwarg to set the color
    - add another kwarg label="Power", then, using plt.legend() after the hist
      function, turn on the legend.
    - add a label to the x-axis called "Power [MW]", it's known as the xlabel.
    - add a title called "Half-hourly power meaurements at the substation"

5) what is the average demand of the substation? Numpy is your friend here.

---
Tip 1: Dont forget to use the keyword argument inplace=True to overwirte the
     dataframe with the output of df.set_index().

Tip 2: Plotting with matplotlib can be complicated and takes a lot of practise.
       Data scientists all over the world google how to use matplotlib every
       single time they draw a figure. So you should too!

Tip 3: Numpy lets you perform many mathematical calculations on numpy arrays.

Hint: import matplotlib.pyplot as plt
      plt is a module object that now contains all the functions you need.
      The histogram plotting function is called hist().
      You can add kwargs to this function (you just need to look at the hist
      function documentaiton for the correct word!).
      You can use plt.title() in the next line after plt.hist() and it will
      still change the information on the same figure.
"""
