"""
                         +================+
                        ||  Challenge 6  ||
                        +================+
It's time to load the substation power data (which is in megawatts MW).
1) Using pandas, load the data using fname and make a new variable called df.
2) print the data to see what it is.
3) what dimensions does the data have? Is there a function or attribute you can
    use for this?
4) What do you notice about the df variable? how many columns does it have? Do
    you think the variable headers are a good description?
5) change the headers to a better word that gives insight to what the data is.
    Note, this is quite difficult so there is a detailed hint.
---
Tip: Loading data can often cause an error. There are different types of errors
in python that tell us different things. A common one when loading a file is
called a "FileNotFoundError", which very cleverly tells you that it couldn't
find the file you asked for. You can test this by doing some nonsense like:
    pd.read_csv("nonsense")
If you are getting this error when using your variable fname, your path must be
wrong.

Tip2: when loading with pd.read_csv(), you build what is known as a dataframe,
this is often shortened to df in examples.

Tip3: it is good practise to describe the actual variable and units when naming
a pandas column. E.g., if we were measuring temperature, instead of a column
that is called 'how_hot', it would be better to say 'temperature_celcius'.

Hint: check your fname matches the actual location of the data.

Hint 2: the df variable is a Dataframe object. Dataframes have attributes that
can tell you interesting things about the object, lets consult google again:
    try googling "dataframe attributes", what interesting information can you
    find, e.g. df.columns

Hint 3: renaming a column name can be complicated, especially when you have a
    lot of columns! The best method is with the Dataframe function df.rename().
    This lets you overwrite specific attributes:
        df.rename(columns={'substation':'new_column_name'}, inplace=True)
    We use the keyword argument 'inplace = True' to tell python to overwirte
    our df object with the output of this function, we could ignore this if we
    instead did:
        df = df.rename(columns={'substation':'power_mw'})
"""
