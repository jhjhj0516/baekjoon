from collections import deque

n = int(input())
queue = deque([k for k in range(1, n+1)])

while len(queue) > 1 :
  queue.popleft()
  word = queue.popleft()
  queue.append(word)

print(queue[0])