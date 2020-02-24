#The start of the text adventure game and i have to make a rubric

print("Find A Way Out Text Game")

#commands of players
answer_A = ["A"]
answer_B = ["B"]
answer_C = ["C"]
yes = ["yes"]
no = ["no"]

required = ("Use only A, B, or C")

#Scenerio
def intro():
    print("Instructions: In order to play this game, type in the choices A, B, C")
    print("You are walking with you class for a camping trip in the woods and you wandered off accidently. When you looked around, you find yourself all by yourself and lost. What will you do?")
    print(""" A. Wander around""" )
    print(""" B. Wait here til someone come""" )
    print(""" C. Use the map that your teacher gave you and follow the map""" )
    choice = input("> ")
    if choice in answer_A:
      option_hungry()
    elif choice in answer_B: 
      game_over()
    elif choice in answer_C: 
      option_go()
    else:
      print(required)
      intro()

def option_go():
    print("You are following the map to Point A and when you kept walking, you see two bridges. An unstabled one and one in ruins. What will you choose?")
    print(""" A. Take the unstabled bridge  """)
    print(" B. Take the ruins bridge" )
    choice = input("> ")
    if choice in answer_A:
      game_over()
    elif choice in answer_B:
      option_hungry()

def option_hungry():
    print("You've been walking for awhile and you start to feel hungry. You discover berries, the only food you can find. Will you eat it?")
    print(""" A. Hell nah """)
    print(""" B. It never hurts to try """)
    choice = input("> ")
    if choice in answer_A:
      option_encounter()
    elif choice in answer_B:
      game_over()
    else:
      print(required)
      intro()

def option_encounter():
    print("You are almost there to your destination. But then you encounter a group of wolves growling at you. What will you do?")
    print(""" A. Grab the nearest thing near you and attack them with that""" )
    print(""" B. Climb up the nearest tree""")
    print(""" C. Run away as fast as you can to the cave""")
    choice = input("> ")
    if choice in answer_A:
      game_over()
    elif choice in answer_B:
      option_tree()
    elif choice in answer_C:
      option_cave()
    else:
      print(required)
      intro()

def option_tree():
    print("You waited for awhile and you see its getting dark. You are not sure if the wolves are still waiting for you. What should you do?")
    print(""" A. Just stay here and sleep til morning rises""")
    print(""" B. I think I should go down now and maybe go to the cave where its more safer""")
    print(""" C.  """)
    choice = input("> ")
    if choice in answer_A:
      option_wakeup()
    elif choice in answer_B:
      option_cave()

def option_cave():
    print("You take shelter in the cave and decided to go to sleep. Enter A to continue the story")
    choice = input("> ")
    if choice in answer_A:
      option_wakeup()

def option_wakeup():
    print("You wake up and go back to the trail. It seems like your almost there. While walking, you encounter a man in a forest.")
    print(" A. Maybe I should asked him for help")
    print(" B. Stranger danger. Keep going and avoid eye contact")
    choice = input("> ")
    if choice in answer_A:
      game_over()
    elif choice in answer_B:
      option_destination()

def option_destination():
    print("It seems forever of a walk, but all the sudden you recognize the area. It seems like you survived and finally out of the forest.")


def game_over():
    while True:
      choice = input("It seems that the choice you made had led you to death or never finding your way out of the woods. Do you want to play again? (enter yes or no) ")
      if choice == 'yes':
        intro()
      elif choice == 'yes':
        print("Goodbye!")
      else:
        print("this isn't yes or no")

intro()
#game over
#def game_over():
  #print("Do you want to play again? (y/n)")
  #choice = input("> ")

#while choice != "y" and choice !="n":
  #if choice == "y":
   # intro()
  #elif choice == "n":
  #  exit(0) 