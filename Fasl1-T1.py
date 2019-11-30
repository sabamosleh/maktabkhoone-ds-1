count=int (input())
numbers=list(map(int,input().split()))
firstQ=1
for q in numbers:
    firstQ*=q

print (int (1000/firstQ))
