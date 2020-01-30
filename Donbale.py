no_of_entry=int(input())
numbers=list(map(int,input().split()))
print(numbers)
for i in range(0,len(numbers)-1):
 numbers[i]-=numbers[i+1]
numbers.pop();

print(numbers)