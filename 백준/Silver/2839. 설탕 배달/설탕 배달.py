N = int(input())
kg_three = N // 3
kg_five = N // 5
cnt = []

for i in range(kg_five+1) :
  for k in range(kg_three+1) :
    if N == 5*i + 3*k :
      total = i+k
      cnt.append(total)

if len(cnt) == 0 :
  print(-1)
else :
  print(min(cnt))