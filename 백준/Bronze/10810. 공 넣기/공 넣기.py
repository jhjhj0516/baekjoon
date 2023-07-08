N, M = map(int, input().split())
num_list = [0 for _ in range(N)]

for i in range(1, M+1) :
  start, end, num = map(int, input().split())
  for k in range(start-1, end) :
    num_list[k] = num

for i in range(N) :
  print(num_list[i],  end = ' ')