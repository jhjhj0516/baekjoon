list = [[0 for k in range(101)] for i in range(101)]
num = int(input())
cnt = 0
sum = 0

while cnt != num :
  left, bottom = map(int, input().split())
  for row in range(left, left+10):
    for col in range(bottom, bottom+10):
      list[row][col] = 1
  cnt+=1

for row in range(101) :
  for col in range(101) :
    if list[row][col] == 1 :
      sum += 1

print(sum)
