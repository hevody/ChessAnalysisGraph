#print('-' * 50)
#print('.' * 50)

#10 moves analysis
# if towards white, positive
# if towards black, negative

print('How many moves?')
mgaGalaw = input()
mgaGalaw = int(mgaGalaw) * 2
mgaGalaw = int(mgaGalaw) + 1


print(mgaGalaw)

evals = []
color = 'white'
for number in range(1, mgaGalaw):
    oddOeven = number // 2
    if oddOeven != 0:
        move = number / 2
        move = move + 0.5
        move = int(move)
    else:
        move = number / 2
        move = int(move)
    if number == 1:
        move = number
    
    print(f'What is the value of the evaluation bar for {color}, move #{move}?')
    while True:
        evaluation = input()
        try:
            floatChecker = float(evaluation)
            break
        except ValueError:
            print('ValueError pings!')
            

    if color == 'white':
        color = 'black'
    else:
        color = 'white'
    evaluation = float(evaluation)
    evals = evals + [evaluation]

print(evals)

newEvals = []
for eval in evals:
    if eval == 0.0:
        a = ''
    if eval > 0:
        eval = eval + 1
    elif eval < 0:
        eval = eval - 1
    eval = int(eval)
    newEvals = newEvals + [eval]

print(newEvals)

beautifier = []
# column length = 21
empties = [' '] * 10
mid = '-'

for newEval in newEvals:
    if newEval == 0:
        WholeColumn = empties + ['-'] + empties
        beautifier = beautifier + [WholeColumn]
        continue
    absoluteNewEval = abs(newEval)
    WholeColumn = []
    tuldoks = ['.'] * absoluteNewEval
    #print(tuldoks)
    secondaryEmptiesMultiplier = 10 - absoluteNewEval
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

for indexTwo in range(20):
    for indexOne in range(mgaGalaw - 1):
        
        print(beautifier[indexOne][indexTwo],end='')
    print()