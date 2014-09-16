#Flail, Shield Bow!

#Import
import random

#Intro and name collection
def start():
    name = "User"
    print("Welcome challenger, I expect you came here searching for a battle!")
    print("Great honor will be bestowed upon you if you prevail!")
    print("I prefer to know the names of my victims, what's yours?")
    name = input("> ")
    print("Okay " + name + ", let the battle..... BEGIN!")
    return name

#player chooses his weapon
def choose(name):
    print("================================================")
    print("Only the best of weapons to choose from:")
    print("[F]-Flail, for terrific close range attacks.")
    print("[S]-Shield, you scared?")
    print("[B]-Bow, maintain your distance, and your aim.")
    playerWep = input("So what will your choice be, " + name + "? > ").upper()
    
    compWep = random.randint(0,2)
    if(compWep == 0):
        compWep = "F"
    elif(compWep == 1):
        compWep = "S"
    else:
        compWep = "B"
            
    return playerWep, compWep

#Start the battle!
def battle(playerWep, compWep, name):

    #Same Weapons chosen
    if(playerWep == compWep):
        print("================================================")
        print("Hmmm.... " + name + " we seem to be equally matched")
        again = input("Shall we try this again? [Y] or [N] >").upper()
        if(again == "Y"):
            playerWep, compWep = choose(name)
           
            battle(playerWep, compWep, name)
        else:
            playerWep = ""
            
    
    #If the flail is chosen

    if(playerWep == "F"):
        print("================================================")
        print("Wise choice, a flail can do some real damage! ")
        print(".......")
        if(compWep == "S"):
            print("Gah! My shield is no match for your powerful flail!")
            playerwin = 1
        elif(compWep == "B"):
            print("Mahahaha! 20 arrows take you down before you even got close with that flail!")
            
    #If the shield is chosen
    
    elif(playerWep == "S"):
        print("================================================")
        print("You must be intimidated, hiding behind a shield will not help you!")
        print(".......")
        if(compWep == "F"):
            print("Like i said... your puny shield stood no chance against my flail")
        elif(compWep == "B"):
            print("Well played... my arrows simply cannot penetrate your shield")
            
    #If the Bow is chosen 
    
    elif(playerWep == "B" or playerWep == "b"): 
        print("================================================")
        print("Ah yes, the bow... keeping your distance would be wise...")
        print(".......")
        if(compWep == "F"):
            print("Good choice you made, my flail cant hurt you at that distance.")
            playerwin = 1
        elif(compWep == "S"):
            print("I block those arrows, and now you are done for...")
    
    #Decipher wins
    
    if(playerwin == True):
        print("================================================")
        print("Looks like you won this round, shall we try this again?")
        play = input("[Y] or [N] > ").upper()
        if(play == "Y"):
            playerWep, compWep = choose(name)
           
            battle(playerWep, compWep, name)
        else:
            print("That is okay, I am already a little embarassed...bye!")
           
    else:
        print("================================================")
        print("Dont be upset, you can always try to defeat me again")
        play = input("[Y] or [N] > ").upper()
        if(play == "Y" or play == "y"):
            playerWep, compWep = choose(name)
           
            battle(playerWep, compWep, name)
        else:
            print("That is okay, I'd run home crying too...bye!")        

#Define the main program runnint
def main():
    name = start()
    playerWep, compWep = choose(name)
    battle(playerWep, compWep, name, playerWin, compWin)


#Call function to begin game
main()
    
    

