import math
import os
import random
import re
import sys
n=input()
if n%2!=0:
    print("Weird")
elif n%2==0 and n>=2 and n<=5:
    print("Not Weird")
elif n%2==0 and n>=6 and n<=20:
    print("Weird")
elif n%2==0 and n>20:
    print("Not Weird")
