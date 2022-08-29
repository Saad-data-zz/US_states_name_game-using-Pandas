import turtle
import pandas

screen = turtle.Screen()
#screen title
screen.title("U.S. State Game")

#image path for turtle
image = "blank_states_img.gif"

#add the shape to scrren as image
screen.addshape(image)

#now changing the shape of  turtle
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
#in data we got  the hold on state as attribute and convert into the list
all_states = data.state.to_list()
#prompt window for input the state name
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name:").title()

    #exit the while loop condition
    if answer_state == "Exit":
        #state not guessed by user
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
                #we can get the list of missing state
        #genenrating the cvs for missing states
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")
        break
    #print(answer_state)
    #answer_state in all_state then turtle print the text on the image
    if answer_state in all_states:
        #everytime the user guesses the state correctly it gonna be add the answer_statw into the guessed_state
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        #it gonna check the input data is in the all_state
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x),  int(state_data.y))
        t.write(answer_state)

#generate the CSV of state not guessed
#guessed_states.to_csv("guessed_states_by_user")