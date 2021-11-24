
First = float(input("Enter your first number: "))
Second = float(input("Enter your second number: "))
Third = float(input("Enter your third number: "))
Fourth =float(input("Enter your fourth number: "))

if First <= Second:
    First, Second = Second, First
    if Second < Third:
         Second,Third = Third, Second
elif Third <= Fourth:
        Third, Fourth = Fourth, Third

if First <= Second:
        First, Second = Second,First
        if Second < Third:
              Second, Third = Third, Second
if Third <= Fourth:
    Third, Fourth = Fourth, Third

    if First <= Second:
        First, Second = Second, First
elif Second <= Third:
        Second, Third = Third, Second
        if Third <= Fourth:
               Third, Fourth = Fourth, Third

HightoLow = First, Second, Third, Fourth

print("The 4 numbers that you enter from highest to lowest is:",HightoLow)