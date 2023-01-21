f = open('./2022/5.txt', 'r').read().split('\n')
crates = dict()
for i in f:
    if i.find('[')!=-1:
       index = (i.find('[')//4)+1
       print(index)