
# is a comment it dont fuck with code
import random

thingopponentplayed = random.randint(1,3)


thingplayed = input("what do you want to play in rock paper scissors? 1 = rock, 2 = paper, 3 = scissors.")

if thingplayed == "1" and thingopponentplayed == 2:
    print("i played paper, paper win")
elif thingplayed == "2" and thingopponentplayed == 3:
    print("i played scissors, i win")
elif thingplayed == "3" and thingopponentplayed == 1:
    print("I played rock, i win")
elif thingplayed == "1" and thingopponentplayed == 1:
    print("tie")
elif thingplayed == "2" and thingopponentplayed == 2:
    print("tie")
elif thingplayed == "3" and thingopponentplayed == 3:
    print("tie")
elif thingplayed == "1" and thingopponentplayed == 3:
    print("i had scissors, u win")
elif thingplayed == "2" and thingopponentplayed == 1:
    print("i had rock, u win")
elif thingplayed == "3" and thingopponentplayed == 2:
    print("i had paper, u win")
else:
    print("that aint an option relaunch the code")
#def triplet(tung):
    #return tung


#if triplet(2) >= 2:
    #print("hi")
#else:
    #print("bye")

#hi = "what is ur name"

#tungsahur = input(hi + " lil tung")

#print(tungsahur + " is ur name? dat cool")


#if tungsahur == "5" or tungsahur == "five":
    #print("5 is a weird ahh name lowkey")
#elif tungsahur == "not 5" or tungsahur == "not five":
    #print("haha ur name is genuinely not 5 thats so funny")
#else:
    #print("ur name is also not 5")
