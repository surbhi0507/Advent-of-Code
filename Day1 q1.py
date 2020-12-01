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
                


