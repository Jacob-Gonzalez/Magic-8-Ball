# Project Name:  Magic-8-Ball
# Discription:   Build a program that will ask for a users name followed by a yes or no question.  This will simulate a magic 8 ball by producing random answers.
#                Project was provided by Codecademy to test knowledge on basic fundamentals of conditional statements.
# Author:        Jacob Gonzalez (28 July 2023)  
import random

# specify name and question you want the 8 ball to answer, answer choices will be randomized in a later statement
name = input("The Magic 8-Ball knows all.  Please tell me who is speaking:  ")
question = input("Ask a yes or no question and recieve your outcome:  ")
print("")
answer = ""
random_number = random.randint(1, 9)

# test print to determine if random_number is working properly
#print(random_number)

# create if/elif/else statement to run through random answers provided by the 8 ball
if random_number == 1:
    answer = "Yes - definitely"
elif random_number == 2:
    answer = "It is decidedly so"
elif random_number == 3:
    answer = "Without a doubt"
elif random_number == 4:
    answer = "Reply hazy, try again"
elif random_number == 5:
    answer = "Ask again later"
elif random_number == 6:
    answer = "Better not tell you now"
elif random_number == 7:
    answer = "My sources say no"
elif random_number == 8:
    answer = "Outlook not so good"
elif random_number == 9:
    answer = "Very doubtful"
else:
    answer = "Error"

# display final results
# create if/elif/elif/else statement to check if name, question or both is empty
if ((name == "") and (not question == "")):
    print("Question:  ", question, "\nMagic 8-Ball's answer:  ", answer)
elif ((not name == "") and (question == "")):
    print(name, "please ask a yes or no question.")
elif ((name == "") and (question == "")):
    print("Please state your name followed by a yes or no question.")
else:
    print(name, "asks:  ", question, "\nMagic 8-Ball's answer: ", answer)

