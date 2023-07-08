num_list = []
for i in range(10):
    num = int(input())
    num_list.append(num)

div_list = []
cnt_list = []

for i in range(10) :
  div_num = num_list[i] % 42
  div_list.append(div_num) 
    
for k in range(10) :
  if div_list[k] not in cnt_list :
    cnt_list.append(div_list[k])

print(len(cnt_list))