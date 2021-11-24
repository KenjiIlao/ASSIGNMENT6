import random
score = 0


def AddTrain():
    First = float(random.randint(0,99))
    Second = random.randint(0,99)

    print((First), "+", (Second),"= ?")
    answer = int(input("Sagot = "))

    if(First + Second == answer):
        print("Tumpak!!!")
        score = 1
    else: 
     print("BAWI KA NALANG!")
    score = 0
    return score

score = score + AddTrain()
score = score + AddTrain()
score = score + AddTrain()
score = score + AddTrain()
score = score + AddTrain()
score = score + AddTrain()
score = score + AddTrain()
score = score + AddTrain()
score = score + AddTrain()
score = score + AddTrain()


print("Your total score of the addition quiz is " + str(score) + "/10")