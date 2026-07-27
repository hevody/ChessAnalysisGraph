
import os


# this intro :)
print('Welcome to Chess Analyzer and Grapher! (if this word exist lol, now it does)')
print('If you ever slip, do not panic! You can always click "e"')
print('If you want to stop altogether, click "s"')
print('Click enter to continue and Ctrl+C to exit')
input()
os.system('cls')



        

side = 'White'
move = 1
evals = []
while True:
    print(f'What is the value of the evaluation bar for {side} in move #{move}?')
    evaluation = input()

    if evaluation == 's':
        break 

    # the part where someone makes mistakes and second-chance is given, this will auto-pop the previous response
    if evaluation == 'e':
        del evals[-1]
        while True:
            print('New value?')
            newVal = input()
            try:
                float(newVal)
                break
            except ValueError:
                print('[*] Value error pings!')
                continue
        newVal = float(newVal)
        evals = evals + [newVal]
        continue

    # error handling if the given value is not float
    try:
        float(evaluation)
    except ValueError:
        print('[*] Value error pings!')
        continue

    evaluation = float(evaluation)

    # adds the given value to the list
    evals = evals + [evaluation]


    # flip sides
    if side == 'White':
        side = 'Black'
    else:
        side = 'White'
        move = move + 1

print(evals)

print('Anything to edit? (y)es or (n)ope')
editQuestion = input()

number = 1
if editQuestion == 'y':
    for editableContent in evals:
        print(f'{number}. {editableContent}')
        number = number + 1
    print("Instruction: Just type the number! before the one you are suppose to edit. Tip: Multiply the move by 2 and it's somewhere near!")
    while True:
        print('Type the number, if finish click (s)')
        numberPick = input()
        if numberPick == 's':
            break
        print('What is the true evaluation?')
        trueEvaluation = input()
        try:
            float(trueEvaluation)
        except ValueError:
            print('[*] Value error pings!')
            continue
        numberPick = int(numberPick)
        trueEvaluation = float(trueEvaluation)
        evals[numberPick - 1] = trueEvaluation

newEvals = []
for eval in evals:
    if eval > 0:
        eval = eval + 1
    elif eval < 0:
        eval = eval - 1
    eval = int(eval)
    newEvals = newEvals + [eval]

beautifier = []
empties = [' '] * 15

for newEval in newEvals:
    if newEval == 0:
        WholeColumn = empties + ['-'] + empties
        beautifier = beautifier + [WholeColumn]
        continue
    absoluteNewEval = abs(newEval)
    WholeColumn = []
    tuldoks = ['.'] * absoluteNewEval
    #print(tuldoks)
    secondaryEmptiesMultiplier = 15 - absoluteNewEval
    secondaryEmpties = [' '] * secondaryEmptiesMultiplier
    #print(secondaryEmpties)
    primaryColumn = tuldoks + secondaryEmpties 
    #print(primaryColumn)
    if newEval > 0:
        primaryColumn.reverse()
        WholeColumn = primaryColumn + ['-'] + empties
        #print(WholeColumn)  
    if newEval < 0:
        WholeColumn = empties + ['-'] + primaryColumn
    print(WholeColumn)
    beautifier = beautifier + [WholeColumn]

print(beautifier)

for indexTwo in range(31):
    for indexOne in range(len(evals)):
        print(beautifier[indexOne][indexTwo], end='')
    print()
input()