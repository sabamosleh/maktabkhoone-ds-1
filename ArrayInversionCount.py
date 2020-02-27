A=[]
k=0
no_of_liens=(int(input()))

for i in range(0,no_of_liens):
    A.append(input())

def count(A,start,mid,end):

     if end-start==1:
         if int(A[start])>int(A[end]):
             global k
             k=k+1
     elif mid+1==end:
         for i in range(start,end):
                 if int(A[i])>int(A[end]):
                     k=k+1

     else:

             for i in range(start,mid+1):
              for j in range(mid+1,end+1):
                     if int(A[i])>int(A[j]):
                      k=k+1



def countInversion(A,start,end):


    if start < end:
        mid=(end+start)//2
        countInversion(A,start,mid)
        countInversion(A,mid+1,end)
        count(A,start,mid,end)



countInversion(A,0,len(A)-1)
print(k%100000)