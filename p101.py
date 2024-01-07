import random

response = "y"
while response == "y":
    no = random.randint(1,6)
    if no == 1:
        print("number on the dice is 1")
    elif no == 2:
        print("number on the dice is 2")
    elif no == 3:
        print("number on the dice is 3")
    elif no == 4:
        print("number on the dice is 4")
    elif no == 5:
        print("number on the dice is 5")
    elif no == 6:
        print("number on the dice is 6")

    response= input("press y to roll again and n to exit")
    print("\n")
    
    
        

 


