"""Draw the electron structure of an element."""
import turtle
import os
import pandas as pd
import math

# Global constants that influence the whole model
BCKG_COL = "#708090"
LINE_COL = "white"
FILL_COL = "#C0C0C0"
ELECTRON_FILL = "#FFFFFF"
TITLE_COL = "red"
ATOM_RADIUS = 30
SHELL_RADIUS = 100
SHELL_GAP = 50
ELECTRON_RADIUS = 7
DRAW_SPEED = 0  # 0 is fastest

# size the screen to fit the largest element (8 shells)
box = 2 * (SHELL_RADIUS + (8 - 1) * SHELL_GAP)
turtle.screensize(canvwidth=box + ATOM_RADIUS * 2, canvheight=box + ATOM_RADIUS * 2 + 20)


def draw_element(element: str):
    """Draw the electrons of an atom."""
    try:
        # security on the input arguments
        if not isinstance(element, str):
            raise TypeError("element should be a string.")
        # set the screen size
        # Change the background colour the specified color
        turtle.bgcolor(BCKG_COL)
        # start with the pen up
        turtle.penup()
        # don't show the turtle
        turtle.hideturtle()
        # set the speed
        turtle.speed(speed=DRAW_SPEED)

        # calculate number of electrons
        electron_arrangement = get_n_electrons_and_shells(element)
        n_shells = len(electron_arrangement)

        # draw central atom
        draw_circle(0, -ATOM_RADIUS, ATOM_RADIUS, LINE_COL, FILL_COL)

        # draw the ionic shells
        draw_shells(n_shells)

        # draw the electrons
        draw_electrons(electron_arrangement)

        # add some text
        turtle.pencolor(TITLE_COL)
        turtle.goto(0, -10)
        turtle.write(element.upper(), True, align="center")

    # catch any errror
    except BaseException:
        raise
    # always finishe the turtle
    finally:
        # finish the drawing
        turtle.done()

    return None


def get_n_electrons_and_shells(element):
    """Get the number of electrons and shells."""
    # load the electron data
    df = load_electron_data(element)
    # get the electron arrangement. This is a string!
    # 2, 8, 8, 2 means that there are 4 shells with 2, 8, 8, 2 electrons each
    electron_arrangement = df.n_electrons.split(",")
    # convert from string to numer
    return [int(electron) for electron in electron_arrangement]


def load_electron_data(element):
    """Load the electron data."""
    # specify the file path
    fname = os.path.join(os.getcwd(), "data", "electrons_per_element.txt")
    # load the data with tab delimiter (note that one entry uses commas!)
    df = pd.read_csv(fname, sep="\t")
    # make the column a nicer name
    df.rename(columns={"No. of electrons per shell": "n_electrons", "Element": "element", "Group": "group", "Z": "z"}, inplace=True)
    # make the elements lower case.
    # extract the elements to a list, making lower case
    elements = []
    for el in df.element.tolist():
        # make lower case
        elements.append(el.lower())
    # overwrite the data
    df["element"] = elements
    # check the element exists
    if element not in df.element.tolist():
        raise ValueError(f"{element} is not recognised, please pick from list: {df.element.tolist()}")
    # set the index
    df.set_index("element", inplace=True)
    # extract data for this element
    element_data = df.loc[element]
    return element_data


def draw_circle(x: int, y: int, r: int, pencolor: str, fillcolor: str = None):
    """Draw a circle with the turtle."""
    # set the line color
    turtle.pencolor(pencolor)
    # go to the start point
    turtle.goto(x, y)
    # start drawing
    turtle.pendown()
    # if there isn't a fill color, just draw the circle
    if fillcolor is None:
        turtle.circle(r)
    else:
        # else there is a fill color.
        turtle.fillcolor(fillcolor)
        turtle.begin_fill()
        turtle.circle(r)
        turtle.end_fill()
    # always end penup
    turtle.penup()
    return None


def draw_shells(n_shells):
    """Draw the rings."""
    # loop through each ring
    for n in range(n_shells):
        # get this shell's radius
        r = shell_radius(n + 1)
        # draw the ring, the start point is 1 radius below (0, 0)
        draw_circle(0, -r, r, LINE_COL)
    return None


def shell_radius(n):
    """Return the radius of the n-order shell."""
    return SHELL_RADIUS + (n - 1) * SHELL_GAP


def draw_electrons(n_electrons):
    """Draw the electrons."""
    # radius of an electron
    r_elec = ELECTRON_RADIUS

    for i, n in enumerate(n_electrons):
        # i+1 is the shell number. Get the radius
        r_shell = shell_radius(i + 1)
        # find the x, y positions for the centre of all electrons
        xs, ys = xy_points_equally_distributed_on_circle(0, 0, r_shell, n)
        # draw the circle (note that turtle draws from bottom of circle)
        for x, y in zip(xs, ys):
            draw_circle(x, y - r_elec, r_elec, LINE_COL, ELECTRON_FILL)


def xy_points_equally_distributed_on_circle(xc, yc, r, n_points):
    """Find the xy coordinates for n points around the edge of a circle."""
    # pre allocate lists
    xs, ys = [], []
    # find degree gap per point, starting at 0deg at bottom of circle.
    angle_r = (2 * math.pi) / n_points
    # starting position is at 90deg, as this is bottom of the circles
    pos = math.radians(90)
    # loop through each point needed
    for i in range(n_points):
        #
        x = r * math.cos(pos)
        y = r * math.sin(pos)
        xs.append(x)
        ys.append(y)
        pos += angle_r

    return xs, ys


if __name__ == "__main__":
    element = input("Specify element to draw:").lower()
    draw_element(element)
