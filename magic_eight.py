#!/usr/bin/env python3  

"""
Magic 8 ball 

"""

import random

# This list of answers contains 10 affirmative answers, 5 non-commital answer, and 5 negative answers :O
ANSWERS = ["It is certain.", 
            "It is decidedly so.", 
            "Without a doubt.", 
            "Yes – definitely.", 
            "You may rely on it.", 
            "As I see it, yes.", 
            "Most likely.", 
            "Outlook good.", 
            "Yes", 
            "Signs point to yes.", 
            "Reply hazy, try again.", 
            "Ask again later.", 
            "Better not tell you now.", 
            "Cannot predict now.", 
            "Concentrate and ask again.", 
            "Don't count on it.", 
            "My reply is no.", 
            "My sources say no.", 
            "Outlook not so good.", 
            "Very doubtful."]

def usr_input():
	usr_input = input("\nASK YOUR QUESTION YOU MORTAL: ")
	return usr_input

while True:                                                    # iterates over the randomized list of the answers
	question = usr_input()
	if question.lower() == "quit":
		break
	print(random.choice(ANSWERS) + "\n")

print("See You Later!.")
