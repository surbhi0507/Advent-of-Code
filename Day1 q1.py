#Challenge-1
li = [1721,979,366,299,675,1456]
lis = []
for i in li:
    for j in li:
        if i!=j:
            if i+j == 2020:
                ans = i*j
                if ans not in lis:
                    print(i, ' x ', j, ' = ', ans)
                    lis.append(ans)

                    
#Challenge-2
lis = []
for i in li:
    for j in li:
        for k in li:
            if i!=j and i!=k and j!=k:
                if i+j+k == 2020:
                    ans = i*j*k
                    if ans not in lis:
                        print(i, 'x', j, 'x', k, ' = ', ans)
                        lis.append(ans)
                



