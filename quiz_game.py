print("welcome to my computer quiz!")


playing = input("Do you want to play? ")
score = 0

if playing.lower() != "yes":
    quit()

print("Okay! Let's play:)")

answer = input("what does the CPU stand for? ").lower()
if answer == "central processing unit":
    print('correct!')
    score += 1
else:
    print('incorrect')
    #like wise add more questions
answer = input("what does the RAM stand for? ").lower()
if answer == "random access memory":
    print('correct!')
    score += 1
else:
    print('incorrect')

answer = input("what does the ROM stand for? ").lower()
if answer == "ram only memory":
    print('correct!')
    score += 1
else:
    print('incorrect')

print("your got"  + str(score) +  "questions correct!")
print("your got" + str((score / 4) * 100) + "%")


