import sys

N = int(input())
ary = []

for i in range(N) :
  num = int(sys.stdin.readline())
  ary.append(num)

ary.sort()

for i in range(N) :
    print(ary[i])