row=""
no_of_columns=0
translate=dict()
entries=[]
row=""
translate["*****oo*oooo*oo"]="T"
translate["oo*ooo***o*ooo*"]="A"
translate["*ooo*oo*oo*ooo*"]="X"
translate["**o***o*o**ooo*"]="M"
translate["*ooo**o*o**ooo*"]="N"

for i in range(3):
     row=row+input()


no_of_columns=int(len(row)/15)
rowRange=len(row)/3


k=0
for j in range(0,int(len(row)/3),5):
         if k==0:
           c=row[j:j+5]
           k+=1

         if k==1:
           b=row[int(rowRange)+j:int(rowRange)+5+j]
           k+=1

         if k==2:
           d=row[2*int(rowRange)+j:2*int(rowRange)+5+j]
           k=0


         entries.append(translate[c+b+d])


translation=""
for i in range(len(entries)):
    translation=translation+entries[i]

print(translation)


#print(translate[row])