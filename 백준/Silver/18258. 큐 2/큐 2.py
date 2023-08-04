from collections import deque
import sys

N = int(sys.stdin.readline().rstrip())
queue = deque()

for _ in range(N) :
  order = sys.stdin.readline().rstrip()
  if 'push' in order :
    num = int(order[5:])
    queue.append(num)
  elif order == 'pop' :
    if len(queue) == 0 :
      print(-1)
    else :
      print(queue[0])
      queue.popleft()
  elif order == 'size' :
    print(len(queue))
  elif order == 'empty' :
    if len(queue) == 0 :
      print(1)
    else :
      print(0)
  elif order == 'front' :
    if len(queue) == 0 :
      print(-1)
    else :
      print(queue[0])
  elif order == 'back' :
    if len(queue) == 0 :
      print(-1)
    else :
      print(queue[len(queue)-1])