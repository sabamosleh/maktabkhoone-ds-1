inputNumber=input()
inputs=[]
inputs.append(input())
inputs=inputs[0].split(" ")

holder=list()
c_max=g_max=0
holder.append(0)

for i in range (1,int(inputNumber)):
    # print(int(inputs[int(holder[len(holder)-1])]))
    # if int(inputs[int(holder[len(holder)-1])]) < int(inputs[i]):
    print("mmmm---->",int(inputs[holder[len(holder)-1]]))
    if int(inputs[len(holder)-1]) < int(inputs[i]):
        holder.append(i)
    elif not holder:
        c_max=int(inputs[i])*i
        if c_max>g_max:
         g_max=c_max
    else:
           if len(holder)>1:

            top=int(holder.pop())
            print("top: "+str(top)+"")
            print("holder: ",holder)
            print(str("i: ")+str(i))
            print("width: ")
            print((i-int(holder[len(holder)-1])-1))
            c_max=int(inputs[top])*(i-int(holder[len(holder)-1])-1)
            if len(holder)==1:
             holder.append(i)
            if c_max>g_max:
                g_max=c_max

while holder:
    global i
    top=int(holder.pop())
    c_max=int(inputs[top])*(i-int(holder[len(holder)-1])-1)
    i=i-1
    if c_max>g_max:
       g_max=c_max




print(holder)
print(inputs)
print(c_max)
print(g_max)