puzzle = []
sum = 0
puzzle = input("Informe a sequencia de números: ")
for index in range(len(puzzle)):
    if (index + 1) == len(puzzle):
        if puzzle[index] == puzzle[0]:
            sum += int(puzzle[index])
    else:
        if puzzle[index] == puzzle[index+1]:
            sum += int(puzzle[index])

print(sum)
