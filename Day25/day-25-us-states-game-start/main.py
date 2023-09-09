import turtle
import pandas as pd
screen = turtle.Screen()


image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

df = pd.read_csv("50_states.csv")
game_is_on = True
tur = []
x = 0
all_state = df.state.to_list()
print(all_state)
input_states = screen.textinput("States Test Game","Input States Name:" )
if input_states in all_state:
    print(input_states)
#while game_is_on:
#    input_states = screen.textinput("States Test Game","Input States Name:" )


#    if input_states in all_state:
#        print(f"{df.state[x]} {input_states}")
#        tmp = turtle.Turtle()
#        tmp.penup()
#        tmp.hideturtle()
state_data = df[df.state == input_states]
print(state_data.state.item())
#        tmp.goto(int(df[df.state == input_states].x), int(df[df.state == input_states].y))
#        tmp.write(f"{input_states}")
#    elif input_states == "quit":
#        game_is_on = False





screen.exitonclick()