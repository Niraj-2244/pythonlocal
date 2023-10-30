name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come an end you can go left or right. Which way eould you like to go? ")

if answer == "left":
    answer = input("you come to a river, you can walk around it or swim accross?  Type walk to walk around and swim to swim accross: ")
    if answer == "swim":
        print("you swam accross and were eaten by an alligator.")
        
    elif answer == "walk":
        print("you walked for many miles, ran out of water and you lsot the game.") 
    else:
        print('Not a valid option. You lose!.')


elif answer == "right":
    answer = input("you come to bridge, it looks woobly, do you want to cross it or head back(cross/back)?")
    if answer == 'back':
        print("you go back you loose.")

    elif answer == 'cross':
        answer = input("you cross the bridge and meet a stranger. Do you talk to them(yes/no)?")

        if answer == 'yes':
            print("you talk to stranger and they give you gold. you WIN!")

        elif answer == 'no':
            print("ypu ignore the stranger and they are offended and you lose.")

        else:
            print("not a valid option. you lose.")

    else:
        print("not a valid option. You lose.")

else:
    print('not a valid option. you lose')