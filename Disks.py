dicks=dict()
Merge="Merge"
Height="Height"
data=[]
output=[]
lendth=input()


for i in range (0,int(lendth)):
    data.append(input())

for i in range(0,len(data)):
        if(data[i].startswith(Merge)):
            src=int(data[i].split(" ")[1])
            dest=int(data[i].split(" ")[2])
            if src  not in dicks.keys():
                dicks[src]=str(src)
            if dest not in dicks.keys():
                dicks[dest]=str(dest)
        if data[i].startswith(Height):
            value=(data[i].split(" ")[1])
            if value not in dicks.keys():
                dicks[int(value)]=str(value)

for i in range(0 ,len(data)):
        if(data[i].startswith(Merge)):
            src=int(data[i].split(" ")[1])
            dest=int(data[i].split(" ")[2])
            for k,v in dicks.items():

                if str(src) in v:
                    src_key=k

                if str(dest) in v:
                   dest_key=k
            if dest_key!=src_key:
                dicks[dest_key]=dicks[dest_key]+','+dicks[src_key]
                # dicks[dest_key]=dicks[src_key]+','+dicks[dest_key]
                dicks[src_key]=''



        else:
            if data[i].startswith(Height):
                value=(data[i].split(" ")[1])

                for k,v in dicks.items():
                    if value in v:
                        if len(str(v).split(','))>1:
                           arr=str(v).split(',')
                           output.append(str(arr.index(value)+1))
                        else:
                            output.append(str(1))

for j in range(0,len(output)):
         print(output[j])
# else:
#      if data[0].startswith(Height):
#          value=(data[0].split(" ")[1])
#          print(1)
