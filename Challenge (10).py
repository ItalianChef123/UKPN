"""
                         +=================+
                        ||  Challenge 10  ||
                        +=================+
Lets try visualising the data.

Pandas dataframes have really helpfully built a method that interacts with the
most common data visualisation tool in python: matplotlib.

1. Try out the most simple technique of df.plot()

The method df.plot() takes many arguments that get passed along to matplotlib.
There is a very long list of things that can be edited by matplotlib. Take a
look at the plot documentation:
    https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html

2. using keyword arguments (kwargs) passed into df.plot(),
    Try make the following changes, using the above webpage to find the correct
    keyword argument to use:
    a) add a title saying "Power at the substation"
    b) add a label on the y axis saying "Power [MW]"
    c) add a label on the x axis saying "Time"
    d) change the line color to red
    e) change the line thickness to 0.5
---
Tip: sometimes matplotlib plots behind the scenes, if nothing popped up, use
      plt.show() to force it to visualize.

Tip 2: All functions in python take either an argument (args) or keyword args
    (kwargs). Args are REQUIRED, kwargs are OPTIONAL. The main difference is
    that we must name the kwarg and use an = sign. e.g. df.plot(title="title").
"""
