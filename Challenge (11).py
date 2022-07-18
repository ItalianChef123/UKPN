"""
                         +=================+
                        ||  Challenge 11  ||
                        +=================+
You sent us some interesting code as an example that uses the turtle package.
From looking at this, we noticed that you would really benefit from a concept
that is known as DRY code. This stands for "Don't repeat yourself".

Usually, if you find yourself copying and pasting the same block of code again
and again, you can apply the DRY code concept. This is when we start to use
functions!

Using the turtle package on a white background,
    1) draw a black unfilled circle starting at (0, -130) with a radius of 130
    2) draw a red unfilled circle starting at (0, -200) with a radius of 200

What you have done here is draw a circle TWICE! This should be your mental
trigger to apply DRY code.

Can you make a function that draws an unfilled cirlce?
    1) what input variables do you need to know?
    2) make the function


Now, using your new function, repeat the first part of this challenge!

Can you make a new function that draws filled circles?

Try adding the nucleus of the atom by drawing a filled circle at (0, -50) with
a radius of 50.

Now, with all functions, they deserve COMMENTS!
Immediately after the definition line, there should be a 'docstring'.
Python has a few suggestions of how formatting of your code should be, these
are called Python Enhancement Proposals (PEP). They are proposed by the
community, for the community. They are not enforced, but recommended.
Read up on what PEP is, and how you might like to use it in your code.
    - PEP8 is the most commonly used proposal, it tells you how to format your
        code.
    - PEP257 has suggestions on how to use docstrings.

---
Tip: it's always best to start your function with a good name and a good order
    and names for your args. Optional arguments can become kwargs for example,
    you could make pencolor a kwarg by setting a default value pencolor='black'
    This way, if you don't specify a pen color, it will just default to black.
    kwargs must come at the end.

Tip: notice how to make your circle in the centre, it always starts at -r?
    draw_circle(x, -r, r).

Hint: don't be afraid to ask for help :)
"""
