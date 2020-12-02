## Part-1

puzzle_ans = []
puzzle = open('input.txt', 'r')

for i in puzzle.read().split("\n"):
    puzzle_ans.append((i.split(' ')[0].split('-')[0], i.split(' ')[0].split('-')[1], i.split(' ')[1].replace(':', ''), i.split(' ')[2]))
#print(puzzle_ans)

answer = []

for x in puzzle_ans:
    password = str(x[3])
    low = int(x[0])
    high = int(x[1])
    check = str(x[2])
    if password.count(check) >= low and password.count(check) <= high:
        answer.append(password)


l = len(answer)
print(l)




#Part-2

puzzle_ans = []
puzzle = open('input.txt', 'r')

for i in puzzle.read().split("\n"):
    puzzle_ans.append((i.split(' ')[0].split('-')[0], i.split(' ')[0].split('-')[1], i.split(' ')[1].replace(':', ''), i.split(' ')[2]))
#print(puzzle_ans)

answer = []


for x in puzzle_ans:
    password = str(x[3])
    low = int(x[0])
    high = int(x[1])
    check = str(x[2])
    if password[low-1] == check and password[high-1] != check:
        answer.append(password)

    elif password[low-1] != check and password[high-1] == check:
        answer.append(password)

l = len(answer)
print(l)












    
