import random
import time

command = ["tell me about you", "show command list", "say hello", "change my name", "tell me a joke", "lets play minigame", "give me a fact", "good bye"]

facts = [
    ["Hot water will turn into ice faster than cold water."],
    ["The Mona Lisa has no eyebrows."],
    ["Ant's take rest for around 8 Minutes in 12 hour period."],
    ["It is physically impossible for pigs to look up into the sky."],
    ["It is impossible for most people to lick their own elbow."],
    ["A crocodile cannot stick its tongue out."],
    ["1 in 5,000 north Atlantic lobsters are born bright blue."],
    ["Falling in love is like being on drugs."],
    ["A happy heart is a healthy heart."],
    ["Every second, your body produces 25 million new cells."],
    ["The best place in the world to see rainbows is in Hawaii."],
    ["Indonesia is home to over 100 endangered animals"],
    ["The world’s biggest flower lives in Indonesia"],
    ["Indonesia is made up of 17,504 islands"]
]

jokes = [
    ["Why do ducks have feathers?", "to cover their butt quacks!:)"],
    ["How do you measure a snake?", "In inches—they dont have feet."],
    ["When does a joke become a dad joke?", "When it becomes apparent"],
    ["What kind of shorts do clouds wear?", "Thunderpants"],
    ["What did one ocean say to the other ocean?", "Nothing, it just waved."],
    ["Do you want to hear a construction joke?", "Sorry, I’m still working on it"],
    ["What do you call a fake noodle?", "An imppasta"],
    ["A man tells his doctor, “Doc, help me. I’m addicted to Twitter!'”", "The doctor replies, “Sorry, I don’t follow you …” "]
]

call = 0

print("\nTurning On..")                                                           
time.sleep(2)
print("\n----------------------------------------\nName\t: Rimuwu >_< Bot\nVersion\t: 1.0\nAuthor\t: MastayY ( Nasywan )\nGithub\t: https://github.com/MastayY\n----------------------------------------")
time.sleep(3)
print("\nRimuwu >_< is turned on and ready to serve you..")
time.sleep(2)
print("\nHello Guest, my name is Rimuwu >_< i'm a bot with feelings ( maybe:v ). Can i know your name?")
time.sleep(2)
name = input("Hello Rimuwu >_< you can call me ")
time.sleep(2)
print("\nOkay so your name is", name, ". Nice to meet you", name, "I'm here to make your day feel better >_<\nBelow is a list of commands that you can use")
time.sleep(1)

print("\nCHATBOT COMMAND LIST")
for i in range(len(command)):
    print(i + 1, "|", command[i])
    
while True:
    print("\nHi", name, ", I'm Rimuwu >_< ")
    userCommand = input("What can I do for you?\n↦ ")
    
    time.sleep(1)
    if (userCommand == command[0]):
        print("\nOutput\n↦\n[ INFO ]\nHello i'm Rimuwu >_< . I'm a chatbot with feelings (maybe :v). my engine name is RMW-01, but I was given a very beautiful name by my dearest creator. Please call me by my name, not my machine name")
    elif (userCommand == command[1]):
        print("\nCOMMAND LIST")
        for i in range(len(command)):
            print(i + 1, "|", command[i])
    elif (userCommand == command[2]):
        print("Output\n↦ Hello", name, "Nice to meet you :)") if (call <= 2) else print("Output\n↦ Stop, I'm starting to feel weird")
        call += 1
    elif (userCommand == command[3]):
        name = input("What should i call you? ")
    elif (userCommand == command[4]):
        print("Rimuwu >_< is thinking...")
        time.sleep(2)
        question = random.randint(0, 7)
        
        print("[ JOKES ]\n", jokes[question][0])
        time.sleep(2)
        print(jokes[question][1], "\nHahaha....")
    elif (userCommand == command[5]):
        print("\n[ MINIGAME LIST ]\n1. Rock Paper Scissor\n2. Guest The Dice Number\n*Input the number not the game name.")
        minigame = int(input("What minigame do you want to play?\n↦ "))
        if (minigame == 1):
            print("\n[ ROCK PAPER SCISSOR MINIGAME ]\n")
            p_score = 0
            c_score = 0

            while True:
                user_choice = input("Enter your choice ( rock / paper / scissor )\n↦ ")
                if user_choice == 'rock' or user_choice == 'paper' or user_choice == 'scissor':
                    com_choice = random.randint(1,3)
                
                    if com_choice == 1:
                        com_choice = 'rock'
                    elif com_choice == 2:
                        com_choice = 'paper'
                    else:
                        com_choice = 'scissor'
                        
                    print("Please wait, Rimuwu >_< is thinking xD ...")
                    time.sleep(2)
                    
                    print("\n====================== Result ===============================")
                    if user_choice == com_choice:
                        print("You choose ",user_choice,"and computer choose ", com_choice)
                        print("Draw!")
                    elif (user_choice == 'rock' and com_choice == 'scissor') or (user_choice == 'paper' and com_choice == 'rock') or (user_choice == 'scissor' and com_choice == 'paper'):
                        print("You choose ",user_choice,"and computer choose ", com_choice)
                        print("You Win!\nYour Score +1")
                        p_score += 1
                    else:
                        print("You choose ",user_choice,"and computer choose ", com_choice)
                        print("You Lose!\nComputer Score +1")
                        c_score += 1
                    print("==============================================================\n")
                    tryAgain = input("Do you want to continue? (Y / N ) ")
                    if tryAgain == "N":
                        break
                else:
                    print("Input Error!")

            print("=========== Score =============\nYour Score\t:",p_score,"\nRimuwu Score\t:", c_score,"\n================================")
        elif (minigame == 2):
            print("[ GUESS THE DICE NUMBER ]\n")
            score = 0
            rounds = int(input("How many games do you want to play?\n↦ "))

            while True:
                if rounds <= 0:
                    print("Game Over")
                    break

                number_choice = int(input("Input your guess (1 - 6) : "))
                print("Dice Rolled....")
                time.sleep(2)
                    
                number = random.randint(1, 6)
                    
                if number_choice == number:
                    print("Cool, You Right")
                    score += 1
                else:
                    print("No, You wrong")
                rounds -= 1
            
            print("=========== Score =============\nScore\t:",score,"\n===============================")
            
        else:
            print("ERROR : Please input only from the list")
    elif (userCommand == command[6]):
        fact = random.randint(0, 13)
        
        print("\n[ INTERESTING FACT ]\n↦", facts[fact][0])
    elif (userCommand == command[7]):
        print("Good Bye", name, "Thanks for Using Rimuwu >_<\nTurning off...")
        time.sleep(3)
        break
    else:
        print("ERROR : The current version of rimuwu's brain can't accept that command >_<")

                    