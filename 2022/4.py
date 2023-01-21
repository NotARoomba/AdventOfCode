overlap = 0
partial = 0
f = [[[int(k) for k in j.split('-')] for j in i.split(',')] for i in open('./2022/4.txt', 'r').read().strip().split('\n')]
for i in f:
    overlap+= (1 if (i[0][0]<=i[1][0] and i[0][1]>=i[1][1]) or (i[1][0]<=i[0][0] and i[1][1]>=i[0][1]) else 0)
    partial+= (1 if ((i[0][0]<=i[1][0] and i[0][1]>=i[1][0]) or (i[1][0]<=i[0][0] and i[1][1]>=i[0][1])) or ((i[1][0]<=i[0][0] and i[1][1]>=i[0][0]) or (i[0][0]<=i[1][0] and i[0][1]>=i[1][1])) else 0)
print(overlap, partial)