f = open('./2022/1.txt', 'r').read().split('\n')
d=[]
t=0
for i in f:
    if i=='':
        d.append(t)
        t=0
        continue
    t+=int(i)
# PART 1
print(sorted(d,reverse=True)[0])
# PART 2
print(sum(sorted(d,reverse=True)[0:3]))