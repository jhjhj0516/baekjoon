
# x에는 월, y에는 일 입력
x, y = map(int, input().split())

# x = int(input())
# y = int(input())

# 31일, 30일, 28일인 달들 리스트 만들기
days_31 = [1, 3, 5, 7, 8, 10, 12]
days_30 = [4, 6, 9, 11]
days_28 = [2]

# 날짜를 모두 더한 변수
days_sum = 0

# x의 직전 달까지의 날을 더함
for month in range(x) :
    if month in days_31 :
        days_sum += 31
    elif month in days_30 :
        days_sum += 30
    else :
        days_sum += 28

# x에 해당하는 날짜인 y도 더함
days_sum += y

# 요일을 구함
if days_sum % 7 == 1 :
    print("MON")
elif days_sum % 7 == 2 :
    print("TUE")
elif days_sum % 7 == 3 :
    print("WED")
elif days_sum % 7 == 4 :
    print("THU")
elif days_sum % 7 == 5 :
    print("FRI")
elif days_sum % 7 == 6 :
    print("SAT")
elif days_sum % 7 == 0 :
    print("SUN")