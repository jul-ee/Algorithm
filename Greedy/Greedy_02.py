#Greedy_02
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]
result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)

# 만약 M의 크기가 100억 이상으로 커진다면?
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

count = int(m / (k + 1)) * k  # 가장 큰 수가 더해지는 횟수
count += m % (k + 1)  # M이 (K + 1)로 나누어 떨어지지 않는 경우

result = 0
result += (count) * first
result += (m - count) * second

print(result)