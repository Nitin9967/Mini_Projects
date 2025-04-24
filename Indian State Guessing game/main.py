import turtle
import pandas

s = turtle.Screen()
s.title("India's States Game")
image = "./map.gif"
s.setup(width=1.0, height=1.0)
s.addshape(image)
turtle.shape(image)

data = pandas.read_csv("./States_name.csv")

def get_state_name():
    return s.textinput(title=f"{len(guessed_states)}/28 States Correct", prompt="What's another state's name?").title()

guessed_states = []
while len(guessed_states) < 50:
    name = get_state_name()
    if name ==  "Exit" :
        break

    if name in guessed_states:
        print("State already guessed.")
    elif name in data["state"].values:
        guessed_states.append(name)

        state_details = data[data["state"] == name]
        x = int(state_details["x"])
        y = int(state_details["y"])

        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.goto(x, y)
        t.write(name, align="center", font=("Arial", 12, "normal"))
    else:
        print("Invalid state name.")

Unguessed_names = []
for names in guessed_states:
    for state in data["state"]:
        if names == state:
            pass
        else:
            Unguessed_names.append(state)
print(Unguessed_names)


s.exitonclick()
