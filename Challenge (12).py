"""
                         +=================+
                        ||  Challenge 12  ||
                        +=================+
This challenge is one of reading some code.

You sent us some code called Electronic_Structure.py.
The code worked and we could run it and see the result!
This is a great achievement.

A crucial aspect of coding is making your code as easy to follow, understand
and read as possible.
We observed some concepts that you could apply to your code to help make it
easier to follow. The challenges you have performed up to now have all been
designed to familiarise you with the tools you need to do this.

There is a concept in coding called 'refactoring'.
Refactoring is taking some code, and trying to achieve the same result in a
more efficient and readable manner.
Software engineers typically design a quick proof of concept, and once they are
happy, they refactor it for deployment.
Refactoring isn't easy and certainly takes some practise. However, the benefits
usually mean that other people can contribute; this is important for team work
and open source development.

We have taken all the concepts you have learned so far and applied them to your
electronic structure code in a refactoring exercise. We have called the script
the bohr_model.py.

In the last task, you actually performed some refactoring on your code using
DRY principles. You identified that you could make a function to perform the
repetitive task of drawing circles (and there are a lot of circles to draw when
drawing the electron structure of an element!), in your code, you called the
turtle.circle() function 116 times. So your new function is perfect for this
job.

We hope that, using your new skills, you can follow the code in the script
called "bohr_model.py" and understand how this works.

The next challenge is to try and understand the code and how these functions
now work.

Can you follow the code that python will execute the code?

Never be afraid to ask for help! We are always happy to answer any questions!
---
Tip 1: python reads from top to bottom, but does not execute the code when it
       reads the functions, it stores the function in memory for when it is asked
       for.

Tip 2: You will regularly see a line that says:
            if __name__ == "__main__":
       This is a very common line of code. Let me explain why it exists.
       If you run this script, __name__ will be called "__main__" ONLY in the
       script that you run.
       So if you import a script into another script, when python is reading
       that file, __name__ will not be called "__main__". Only the file being
       run is called "__main__".
       This means that, the code after this if statement is only run if you
       specifically told python to run that script, and not when you import it.
       It is handy, because you could import the new draw_circle() function and
       use it again in a new project, without drawing the electron structure.

Tip 3: the first line of code that is excuted is after the if __name__... part.
       So following the code will actually start near the bottom!
"""
