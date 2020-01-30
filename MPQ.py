data=[]
output=[]
input_count=input()
my_mpq=[]

for i in range(0,int(input_count)):
    data.append(input())
my_mpq=list(filter(str.isdigit, data[0]))

for i in range(1,len(data)):
    if(len(my_mpq)%2==0):
        middle=int(len(my_mpq)/2)-1
    else:
          middle=int(len(my_mpq)/2)
    if data[i]=="remove":
        output.append(my_mpq.pop(middle))

    if data[i].startswith("insert"):
        my_mpq.insert(len(data)-1,str(list(filter(str.isdigit, data[i]))[0]))


for j in range(0,len(output)):
    print(output[j])