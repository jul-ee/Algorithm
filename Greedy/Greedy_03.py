# Greedy_03
"""
# min() 함수 이용
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 가장 작은 수 찾기
    min_value = min(data)
    # 가장 작은 수 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result)
"""
# 2중 반복문 구조 이용
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    # 1 <= 카드의 숫자 <= 10000 인 자연수이므로
    min_value = 10001
    for j in range(m):
        min_value = min(min_value, i)
    result = max(result, min_value)

print(result)