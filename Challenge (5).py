"""
                         +================+
                        ||  Challenge 5  ||
                        +================+
Back to the code.
Pandas is a package that, behind the scenes, uses numpy to load stuff. For that
reason, using pandas is preferable if the data is tabular.
But first, we need to specify the file name.

We have provided a file called 'test_data_for_oli.csv'. But it is inside a sub-
directory. Let's learn the most useful package for filenames: os.
1) Load the os package.
2) make a variable called 'fname' that is the file path of your data file.
---
Tip: A time series is a variable that changes with time. Most things can be
expressed as a time series. E.g. the temperature for the last year, or in our
example, the power at a substation for roughly 18 months.

Tip2: os stands for 'operating system', like windows, mac OS, or linux. This
module helps us build code that works on all operating systems. One of the
biggest challenges for software developers is file paths, because they all use
different conventions.

Hint: remember, googling "build a filepath with os python" will usually give
you a worked example.

Hint2: the best function for this is os.path.join()

Hint3: a really useful function is os.getcwd(), this gives you the file path of
your 'current working directory'. When using os.path.join, it will assume that
you are telling python to start looking from wherever your CWD is. A clever way
to build full file paths is to use os.path.join starting with os.getcwd():
    fname = os.path.join(os.getcwd(), "data" ...)

"""
