import os
choice = input("shutdown your computer? (y or n)")
if choice =='y' or choice == 'Y':
    os.system("shutdowm /s ")
else:
    print("Exiting the program")
    