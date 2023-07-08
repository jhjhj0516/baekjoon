N = int(input())
M = list(map(int, input().split()))
v = int(input())
num_cnt = 0

for i in range(N) :
  if v == M[i] :
    num_cnt += 1

print(num_cnt)