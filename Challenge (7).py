"""
                         +================+
                        ||  Challenge 7  ||
                        +================+
Pandas has some cool functions to quickly understand the data.
df is currently a dataframe object.
Dataframe objects have their own methods. You can see them on the pandas site
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html, scroll down
past attributes to the methods section. There are some useful ones like .max()
and .mean().

1) find the maximum values in the dataframe.
2) Use the values attribute to extract the numpy array from the dataframe.

---
Tip: you can find out what the object type is using the type(df) function. Here
    we see that df is a pandas.core.frame.DataFrame, the last bit is the
    important bit. It is a DataFrame object. Because this object has in-built
    attibutes and methods, we can access them using the . after the object.
    Attributes do NOT have brackets, methods DO have brackets.
    If you add brackets after an attribute, you will get a TypeError saying
    that the object is not callable. This can be a common headache in python!

    For example, df.values returns the numpy array of the data. This is very
    useful if you want to use numpy techniques, e.g. np.sum(df.values). Note
    that .values is an attribute, not a method. You cannot df.values()! because
    that is like trying to use a numpy array as a function, but it isn't one.
"""
