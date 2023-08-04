import sys

N = int(sys.stdin.readline())
num_list = []
new_list = []

for i in range(N) :
  num_list.append(int(sys.stdin.readline()))
    
for i in range(0, N) :
  if len(new_list) == 0 or new_list[-1] < num_list[i]:
    new_list.append(num_list[i])
    continue

  for k in range(0, len(new_list)) :
    if num_list[i] < new_list[k] :
      new_list.insert(k, num_list[i])
      break
        
for num in new_list :
  print(num)