inputNumber=input()
inputs=[]
inputs.append(input())
inputs=inputs[0].split(" ")

# for i in range(int(inputNumber)):
#     inputs.append(inputs[i])
# print(inputs)

max_area=0
def max_area_histogram(histogram):

    stack = list()

    index = 0
    while index < len(histogram):


        if (not stack) or (histogram[stack[-1]] <= histogram[index]):
            stack.append(index)
            index =index+1

        else:
            # pop the top 
            top_of_stack = stack.pop()

            area = int((histogram[top_of_stack] *
                    ((index - stack[-1] - 1)
                     if stack else index)))

            # update max area, if needed
            global max_area
            max_area = max(max_area, int(area))

    while stack:

        # pop the top 
        top_of_stack = stack.pop()

        print(histogram[top_of_stack])
        print((index - stack[-1] - 1))
        area = ((histogram[top_of_stack] *
                ((index - stack[-1] - 1)
                 if stack else index)))

        # update max area, if needed

        max_area = max(max_area, int(area))


    return max_area

# Driver Code 
print( max_area_histogram(inputs))
  