with open('input day3.txt') as file:
    input1 = file.read().split()

# Part-1    

trees = 0
store = []
for i in input1:
    store.append([ch for ch in i])

#print(store)

x = y = 0
while x < len(store):
    if store[x][y] == '#':
        trees += 1
    y += 3
    y = y % len(store[1])
    x += 1
print(trees)


##print(len(store[0]))
##print(store[0])

# Part-2

total_trees = 1
slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
for i in slopes:
    a, b = i
    #print(a, b)
    trees = 0
    x = 0
    y = 0
    while x < len(store):
        if store[x][y] == '#':
            trees += 1
        y += a
        y = y % len(store[1])
        x += b

    total_trees = total_trees * trees

print(total_trees)










##store = []
##for i in input.read().split("\n"): 
##    i.split(' ')
##    li = list(input) #list in list
##    print(li)
##    store.append(li)
##print(store)
##
###i.split(' ')


