# PART 1
rock = 'AX'
paper = 'BY'
scissors = 'CZ'
score = 0
f = [i.split() for i in open('./2022/2.txt', 'r').read().strip().split('\n')]
for i in f:
    if "".join(i) == rock or "".join(i) == paper or "".join(i) == scissors:
        score+=(ord(i[1])-87)+3
    elif ((rock.__contains__(i[0]) and scissors.__contains__(i[1])) or (paper.__contains__(i[0]) and rock.__contains__(i[1])) or (scissors.__contains__(i[0]) and paper.__contains__(i[1]))):
        score+=(ord(i[1])-87)
    else:
        score+=(ord(i[1])-87)+6
print(score)
# PART 2
score = 0
for i in f:
    if i[1]=='Y':
        score+=(ord(i[0])-64)+3
    elif i[1]=='X':
        score+=(3 if (ord(i[0])-65)==0 else (ord(i[0])-65))
    else:
        score+=(1 if (ord(i[0])-63)==4 else (ord(i[0])-63))+6
print(score)