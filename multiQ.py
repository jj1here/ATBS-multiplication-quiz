import pyinputplus as pyip
import random, time

numQuest = 5
correct = 0

for question in range(numQuest) :
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)

    prompt = '#%s: %s x %s = ' %(question+1, num1, num2)
    try:
        pyip.inputStr(prompt, allowRegexes=['^%s$'%(num1*num2)], blockRegexes=[('.*', 'Incorrect')],timeout=8,limit=3)
    except pyip.TimeoutException:
        print("Out of time!")
    except pyip.RetryLimitException:
        print("Out of tries!")
    else:
        print("Correct")
        correct += 1
print(f'Correct answers: {correct} out of {numQuest}')