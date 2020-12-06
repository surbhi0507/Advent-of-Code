# Part-1

lis = []
with open('input day5.txt', 'r') as input:
    for ids in input:
        lis.append(ids.rstrip())
#print(lis)

##with open('input day5.txt') as x:
##    passes = x.read().split()
#print(passes)

def fun(boarding_pass, row_col):
    for i in boarding_pass:
        if i == 'F' or i == 'L':
            row_col[1] = (row_col[0] + row_col[1])//2
            row_col[0] = row_col[0]
        elif i == 'B' or i == 'R':
            row_col[0] = (row_col[0] + row_col[1])//2 +1
            row_col[1] = row_col[1]
        
    if boarding_pass[-1] == 'F' or boarding_pass[-1] == 'L':
        return row_col[0]
    else:
        return row_col[1]

seatId = []
for seat in lis:
    rows = fun(seat[:7], [0,127])
    column = fun(seat[7:], [0, 7])
    seat = rows*8 + column
    seatId.append(seat)
print(max(seatId))

# Part-2
seatId.sort()
num = 1
while num < len(seatId):
    if seatId[num] != seatId[num-1] + 1:
        print(seatId[num]-1)
    num +=1


#print(seatId(passes))
