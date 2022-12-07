import random

player_name=input("Enter your name: ")
wanna_play=input("Hello {} would you like to play a game with us? (YES/NO)".format(player_name))

num=random.randint(1,10)
attempt=0
while wanna_play.lower()=="yes":
    guess=int(input("Select a number between 1 to 10 "))
    try:
        print("rand",num)
        attempt=attempt+1
        if guess<1 or guess>10:
            raise ValueError("Make a guess between 1 to 10 only!!!!")
        if num==guess:
            print("Congratulationsss!!!!  You got it in {} attempts".format(attempt))
            wanna_play=input("Wanna continue the game? (yes/no) ")
            attempt=0
            num=random.randint(1,10)
        elif num>guess:
            print("Just a lil higher")
        elif num<guess:
            print("Make it a lil lower")
    except TypeError:
        pass
if wanna_play.lower()=="no":
    print("Good game! Have a great day ahead")


 