# [1,0,2,-1,-3,-4,4]----ip
# [[-1,0,1],[-4,0,4]]----op

li=[1,0,2,-1,-3,-4,4,9,-9]
for i in range(len(li)):
    for j in range(i+1,len(li)):
        if li[i] + li[j] == 0:
            print([li[i], 0, li[j]])

