N, M = map(int, input().split())
arr = list(map(int, input().split()))
total_list = []

for start in range(N-2) :
  for mid in range(start+1, N-1):
    if arr[start]+arr[mid] >= M :
      pass
    for end in range(mid+1, N) :
      total = arr[start]+arr[mid]+arr[end]
      if total<= M :
        total_list.append(total)

print(max(total_list))