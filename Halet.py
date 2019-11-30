codeBlock1="assign "
codeBlock2="cout "
codeBlock3="goto "
goto_line_rec=0
rec_state=-1
no_of_liens=(int(input()))
codeLines=[]
values_map=dict()

for i in range(no_of_liens):
    codeLines.append(input())

def find_rec(beginIndex,end_index):
    for beginIndex in range(beginIndex,end_index+1):
        if codeBlock3 in codeLines[beginIndex] :
          global goto_line_rec
          goto_line_rec=codeLines[beginIndex].split()
          find_rec(int(goto_line_rec[1])-1,no_of_liens)


def parse_code(beginIndex,end_index):



    for beginIndex in range(beginIndex,end_index+1):

        if codeBlock1 in codeLines[beginIndex]:
           ass_line= codeLines[beginIndex].split()


           if ass_line[3].isnumeric() & ass_line[5].isnumeric():
             values_map[ass_line[1]]=int(ass_line[3])+int(ass_line[5])


           if ass_line[3].isalpha() & ass_line[5].isalpha():
             values_map[ass_line[1]]=values_map[ass_line[3]]+values_map[ass_line[5]]

           if ass_line[3].isnumeric() & ass_line[5].isalpha():
             values_map[ass_line[1]]=int(ass_line[3])+values_map[ass_line[5]]

           if ass_line[3].isalpha() & ass_line[5].isnumeric():
             values_map[ass_line[1]]=int(ass_line[5])+values_map[ass_line[3]]


        if codeBlock2 in codeLines[beginIndex] :
            out_line=codeLines[beginIndex].split()
            if out_line[1].isnumeric() :
                print(out_line[1])
            if out_line[1].isalpha() :
                print(values_map[out_line[1]] % (10**9+7))

        if codeBlock3 in codeLines[beginIndex] :
            goto_line=codeLines[beginIndex].split()
            parse_code(int(goto_line[1])-1,no_of_liens)




try:
    find_rec(0,no_of_liens)
except RecursionError:
    rec_state=1
    print("-1")
except IndexError:
    rec_state=0

if rec_state!=1:
    try:
     parse_code(0,no_of_liens)
    except IndexError:
        exit(0)










           #print(p1)
    # codeLines.append(codeLine)



