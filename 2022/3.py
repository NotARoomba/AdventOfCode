# PART 1
priority = 0
f = [[i[:len(i)//2], i[len(i)//2:]] for i in open('./2022/3.txt', 'r').read().strip().split('\n')]
for i in f:
    for a in i[0]:
        priority+=((ord(a)-96 if a.islower() else ord(a)-38)if not i[1].find(a)==-1 else 0)
        if not i[1].find(a)==-1:
            break
print(priority)
# PART 2
priority = 0
f = open('./2022/3.txt', 'r').read().strip().split('\n')
f = [f[x:x+3] for x in range(0, len(f), 3)]
for i in f:
    for a in i[0]:
        priority+=((ord(a)-96 if a.islower() else ord(a)-38)if i[1].find(a)!=-1 and i[2].find(a)!=-1 else 0)
        if i[1].find(a)!=-1 and i[2].find(a)!=-1:
            break
print(priority)