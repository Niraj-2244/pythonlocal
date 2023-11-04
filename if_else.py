import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input("Enter the number: ").strip())
if (n % 2) == 0:
    if n in range(2, 6):
        print("Number is Not weird.")
    elif n in range(6, 21):
        print("Number is Weird")
    else:
        print("Number is not Weird")
else:
    print("Number is Weird.")
    
#another method same result.
    '''n = int(input())
if n % 2:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")'''