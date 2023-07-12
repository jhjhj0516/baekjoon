years = 1
num_list = [1, 1, 1]
ESM_list = list(map(int, input().split()))

while num_list != ESM_list :
  if num_list[0] + 1 <= 15 :
    num_list[0] += 1
  else :
    num_list[0] = 1
  
  if num_list[1] + 1 <= 28 :
    num_list[1] += 1
  else :
    num_list[1] = 1
  
  if num_list[2] +1 <= 19 :
    num_list[2] += 1
  else :
    num_list[2] = 1

  years += 1

print(years)