#Part-1

with open('input day4.txt') as file:
    input = file.read().split("\n\n")

req_fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']


##input = open('input day4.txt')
##lis=[]
##for i in input.read().split("\r\n"):
##    lis.append(i.split("\n\n"))

valid_pass = 0

for i in input:
    flag = True
    for j in req_fields:
        if str(j+':') not in i:
            flag = False
            break
    if flag == True:
        valid_pass += 1

print(valid_pass)

#Part-2

def checkHeight(height):
    unit = height[-2:len(height)]
    height = height[:-2]
    if not height.isdigit():
        return False
    height = int(height)
    if unit == 'cm' and 150<= height <=193:
        return True
    if unit == 'in' and 59<= height <=76:
        return True
    return False

def checkHair(hair):
    if len(hair) != 7 and hair[0] != '#':
        return False
    if hair[1:].isalnum():
        return True
    return False

def checkEye(eye):
    colors = ['amb','blu','brn','gry','grn','hzl','oth']
    for x in colors:
        if eye == x:
            return True
    return False

def check(values):
    req_fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    for i in req_fields:
        if i not in values:
            return False

    if not 1920 <= int(values['byr']) <= 2002:
        return False
    if not 2010 <= int(values['iyr']) <= 2020:
        return False
    if not 2020 <= int(values['eyr']) <= 2030:
        return False
    if len(values['pid']) != 9 or not values['pid'].isdigit():
        return False
    if not checkHair(values['hcl']):
        return False
    if not checkHeight(values['hgt']):
        return False
    if not checkEye(values['ecl']):
        return False
    return True

strictly_valid_pass=0

for k in input:
    values = {}
    req_fields = k.split()
    #print(req_fields)
    for z in req_fields:
        req, value = z.split(':')
        values[req] = value
    strictly_valid_pass += check(values)


print(strictly_valid_pass)

