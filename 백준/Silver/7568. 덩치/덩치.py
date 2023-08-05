import sys

N = int(sys.stdin.readline())
num_list = []

for _ in range(N) :
  num_list.append(list(map(int,sys.stdin.readline().split())))

cnt = [1 for _ in range(N)]

for i in range(0, N-1) :
  for k in range(i+1, N) :
    if num_list[i][0] > num_list[k][0] and num_list[i][1] > num_list[k][1] :
      cnt[k] += 1

    elif num_list[i][0] < num_list[k][0] and num_list[i][1] < num_list[k][1] :
      cnt[i] += 1

for i in range(len(cnt)) :
  print(cnt[i], end = ' ')