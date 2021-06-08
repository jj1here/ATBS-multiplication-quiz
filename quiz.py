import random

numQuest = 5
correct = 0

for question in range(numQuest) :
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    ans = num1 *num2

    tries =0
    while tries<3 :
        quest = int(input(f'What is {num1} x {num2}\n'))
        if quest == ans :
            print("Correct")
            correct +=1
            break
        else:
            print("Incorrect")
            tries +=1

print(f'You got {correct} out of {numQuest}')

