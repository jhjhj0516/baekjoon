num = int(input())
if 90 <= num <= 100 :
    score = 'A'
elif 80 <= num :
    score = 'B'
elif 70 <= num :
    score = 'C'
elif 60 <= num :
    score = 'D'
else :
    score = 'F'
print(score)