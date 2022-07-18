import turtle

elements = ["Placeholder", "hydrogen", "helium", "lithium", "beryllium", "boron", "carbon", "nitrogen", "oxygen",
            "fluorine", "neon", "sodium", "magnesium", "aluminium", "silicon", "phosphorus", "sulfur", "chlorine",
            "argon", "potassium", "calcium"]
iterations = 0
element = input("Which element from Hydrogen to Calcium would you like to draw? ")
element = element.lower()
electrons = elements.index(element)
turtle.bgcolor("#708090")  # Change the background colour to slate gray
turtle.penup()
turtle.hideturtle()
turtle.goto(0, 0)
turtle.pencolor("white")  # Change the pen colour to white
turtle.fillcolor("#C0C0C0")  # Change the fill colour to silver
turtle.pendown()
turtle.begin_fill()
r = 50
turtle.circle(r)
turtle.end_fill()
turtle.fillcolor("#FFFFFF")  # Change the fill colour to white for the electrons
turtle.penup()
turtle.goto(0, -80)
turtle.pendown()
r = 130
turtle.circle(r)
if electrons >= 2:
    turtle.penup()
    turtle.goto(0, 170)
    turtle.pendown()
    turtle.begin_fill()
    r = 10
    turtle.circle(r)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(0, -90)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()
    electrons = electrons - 2
else:
    turtle.penup()
    turtle.goto(0, 170)
    turtle.pendown()
    turtle.begin_fill()
    r = 10
    turtle.circle(r)
    turtle.end_fill()
    electrons = electrons - 1
while electrons > 0:
    if iterations == 0:
        turtle.penup()
        turtle.goto(0, -170)
        turtle.pendown()
        r = 210
        turtle.circle(r)
        if electrons >= 8:
            r = 10
            turtle.penup()
            turtle.goto(10, 240)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(-10, 240)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(210, 40)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(210, 20)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(10, -180)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(-10, -180)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(-210, 20)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.pendown()
            turtle.begin_fill()
            turtle.goto(-210, 40)
            turtle.circle(r)
            turtle.end_fill()
            electrons = electrons-8
            iterations = iterations+1
        elif electrons == 7:
            r = 10
            turtle.penup()
            turtle.goto(10, 240)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(-10, 240)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(210, 40)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(210, 20)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(10, -180)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(-10, -180)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(-210, 30)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            electrons = electrons-7
            iterations = iterations + 1
        elif electrons == 6:
            r = 10
            turtle.penup()
            turtle.goto(10, 240)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(-10, 240)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(210, 40)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(10, -180)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(-10, -180)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(-210, 30)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            electrons = electrons-6
            iterations = iterations + 1
        elif electrons == 5:
            r = 10
            turtle.penup()
            turtle.goto(10, 240)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(-10, 240)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(210, 40)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(0, -180)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(-210, 30)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            electrons = electrons-5
            iterations = iterations + 1
        elif electrons == 4:
            r = 10
            turtle.penup()
            turtle.goto(0, 240)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(210, 40)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(0, -180)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(-210, 30)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            electrons = electrons-4
            iterations = iterations + 1
        elif electrons == 3:
            r = 10
            turtle.penup()
            turtle.goto(0, 240)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(0, -180)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(-210, 30)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            electrons = electrons-3
            iterations = iterations + 1
        elif electrons == 2:
            r = 10
            turtle.penup()
            turtle.goto(0, 240)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(0, -180)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            electrons = electrons-2
            iterations = iterations + 1
        else:
            r = 10
            turtle.penup()
            turtle.goto(0, 240)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            electrons = electrons-1
            iterations = iterations + 1
    elif iterations == 1:
        turtle.penup()
        turtle.goto(0, -200)
        turtle.pendown()
        r = 240
        turtle.circle(r)
        if electrons >= 8:
            r = 10
            turtle.penup()
            turtle.goto(10, 270)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(-10, 270)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(240, 40)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(240, 20)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(10, -210)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(-10, -210)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(-240, 20)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.pendown()
            turtle.begin_fill()
            turtle.goto(-240, 40)
            turtle.circle(r)
            turtle.end_fill()
            electrons = electrons-8
            iterations = iterations+1
        elif electrons == 7:
            r = 10
            turtle.penup()
            turtle.goto(10, 270)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(-10, 270)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(240, 40)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(240, 20)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(10, -210)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(-10, -210)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(-240, 30)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            electrons = electrons-7
            iterations = iterations + 1
        elif electrons == 6:
            r = 10
            turtle.penup()
            turtle.goto(10, 270)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(-10, 270)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(240, 40)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(10, -210)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(-10, -210)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(-240, 30)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            electrons = electrons-6
            iterations = iterations + 1
        elif electrons == 5:
            r = 10
            turtle.penup()
            turtle.goto(10, 270)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(-10, 270)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(240, 40)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(0, -210)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(-240, 30)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            electrons = electrons-5
            iterations = iterations + 1
        elif electrons == 4:
            r = 10
            turtle.penup()
            turtle.goto(0, 270)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(240, 40)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(0, -210)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(-240, 30)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            electrons = electrons-4
            iterations = iterations + 1
        elif electrons == 3:
            r = 10
            turtle.penup()
            turtle.goto(0, 270)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(0, -210)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(-240, 30)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            electrons = electrons-3
            iterations = iterations + 1
        elif electrons == 2:
            r = 10
            turtle.penup()
            turtle.goto(0, 270)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(0, -210)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            electrons = electrons-2
            iterations = iterations + 1
        else:
            r = 10
            turtle.penup()
            turtle.goto(0, 270)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            electrons = electrons-1
            iterations = iterations + 1
    else:
        turtle.penup()
        turtle.goto(0, -230)
        turtle.pendown()
        r = 270
        turtle.circle(r)
        if electrons >= 8:
            r = 10
            turtle.penup()
            turtle.goto(10, 300)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(-10, 300)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(270, 40)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(270, 20)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(10, -240)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(-10, -240)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(-270, 20)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.pendown()
            turtle.begin_fill()
            turtle.goto(-270, 40)
            turtle.circle(r)
            turtle.end_fill()
            electrons = electrons-8
            iterations = iterations+1
        elif electrons == 7:
            r = 10
            turtle.penup()
            turtle.goto(10, 300)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(-10, 300)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(270, 40)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(270, 20)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(10, -240)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(-10, -240)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(-270, 30)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            electrons = electrons-7
            iterations = iterations + 1
        elif electrons == 6:
            r = 10
            turtle.penup()
            turtle.goto(10, 300)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(-10, 300)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(270, 40)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(10, -240)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(-10, -240)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(-270, 30)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            electrons = electrons-6
            iterations = iterations + 1
        elif electrons == 5:
            r = 10
            turtle.penup()
            turtle.goto(10, 300)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(-10, 300)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(270, 40)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(0, -240)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(-270, 30)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            electrons = electrons-5
            iterations = iterations + 1
        elif electrons == 4:
            r = 10
            turtle.penup()
            turtle.goto(0, 300)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(270, 40)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(0, -240)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(-270, 30)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            electrons = electrons-4
            iterations = iterations + 1
        elif electrons == 3:
            r = 10
            turtle.penup()
            turtle.goto(0, 300)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(0, -240)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(-270, 30)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            electrons = electrons-3
            iterations = iterations + 1
        elif electrons == 2:
            r = 10
            turtle.penup()
            turtle.goto(0, 300)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(0, -240)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            electrons = electrons-2
            iterations = iterations + 1
        else:
            r = 10
            turtle.penup()
            turtle.goto(0, 300)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            electrons = electrons-1
            iterations = iterations + 1

electrons = elements.index(element)
if electrons >= 2:
    structure = ["2"]
    electrons = electrons-2
    if electrons >= 8:
        structure.append("8")
        electrons = electrons - 8
        if electrons >= 8:
            structure.append("8")
            electrons = electrons - 8
            if electrons >= 8:
                structure.append("8")
                electrons = electrons - 8
            elif electrons == 7:
                structure.append("7")
                electrons = electrons - 7
            elif electrons == 6:
                structure.append("6")
                electrons = electrons - 6
            elif electrons == 5:
                structure.append("5")
                electrons = electrons - 5
            elif electrons == 4:
                structure.append("4")
                electrons = electrons - 4
            elif electrons == 3:
                structure.append("3")
                electrons = electrons - 3
            elif electrons == 2:
                structure.append("2")
                electrons = electrons - 2
            elif electrons == 1:
                structure.append("1")
                electrons = electrons - 1
            else:
                pass
        elif electrons == 7:
            structure.append("7")
            electrons = electrons - 7
        elif electrons == 6:
            structure.append("6")
            electrons = electrons - 6
        elif electrons == 5:
            structure.append("5")
            electrons = electrons - 5
        elif electrons == 4:
            structure.append("4")
            electrons = electrons - 4
        elif electrons == 3:
            structure.append("3")
            electrons = electrons - 3
        elif electrons == 2:
            structure.append("2")
            electrons = electrons - 2
        elif electrons == 1:
            structure.append("1")
            electrons = electrons - 1
        else:
            pass
    elif electrons == 7:
        structure.append("7")
        electrons = electrons - 7
    elif electrons == 6:
        structure.append("6")
        electrons = electrons - 6
    elif electrons == 5:
        structure.append("5")
        electrons = electrons - 5
    elif electrons == 4:
        structure.append("4")
        electrons = electrons - 4
    elif electrons == 3:
        structure.append("3")
        electrons = electrons - 3
    elif electrons == 2:
        structure.append("2")
        electrons = electrons - 2
    elif electrons == 1:
        structure.append("1")
        electrons = electrons - 1
    else:
        pass
elif electrons == 1:
    structure = ["1"]
else:
    pass
print(structure)
if turtle.xcor() < -470 or turtle.xcor() > 470 or turtle.ycor() < -390 or turtle.ycor() > 400:
    turtle.penup()
    turtle.goto(0, 0)
turtle.done()
