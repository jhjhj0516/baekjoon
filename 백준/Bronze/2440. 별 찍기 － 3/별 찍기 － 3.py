n = int(input())

for i in range(n) :
    for k in range(n-i) :
        print('*', end='')
    print(end='\n')