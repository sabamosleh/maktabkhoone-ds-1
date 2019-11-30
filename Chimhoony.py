
import numpy as np

no_of_lines = int(input())
lines = ""
inputMap=dict()
for i in range(no_of_lines):
        row=input()
        key=row.split()[0]
        if key in inputMap:
            inputMap[key]+=(','+row.split()[1]+' '+row.split()[2])
        else:
            inputMap[key]=row.split()[1]+' '+row.split()[2]


zeros = [ [0] * 24 for _ in range(60)]

for key in inputMap:
    if '+' in inputMap[key].split(',')[0]:
        enterTime = inputMap[key].split(',')[0].split()[0]
        enterTime_clmn=int(enterTime.split(":")[0])
        enterTime_row=int(enterTime.split(":")[1])


    else:
        exitTime = inputMap[key].split(',')[0].split()[0]
        exitTime_clmn=int(exitTime.split(":")[0])
        exitTime_row=int(exitTime.split(":")[1])


    if '+' in inputMap[key].split(',')[1]:
         enterTime = inputMap[key].split(',')[1].split()[0]
         enterTime_clmn=int(enterTime.split(":")[0])
         enterTime_row=int(enterTime.split(":")[1])


    else:
        exitTime = inputMap[key].split(',')[1].split()[0]
        exitTime_clmn=int(exitTime.split(":")[0])
        exitTime_row=int(exitTime.split(":")[1])


    for j in range(enterTime_clmn,exitTime_clmn+1):
        for i in range(enterTime_row,exitTime_row+1):
            zeros[i][j]+=1


zeros=np.array(zeros)
i,j = np.unravel_index(zeros.argmax(), zeros.shape)

print(str(j)+":"+str(i))




