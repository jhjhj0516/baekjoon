A, B = map(int, input().split())
C = int(input())

if B+C < 60 :
    B = B+C
else :

    if A + (B+C)//60 > 23 :
        A = A + (B+C)//60 - 24
    else :
        A = A + (B+C)//60

    if (B+C) % 60 == 0:
        B = 0
    else :
        B = (B+C) % 60

print(A,B)