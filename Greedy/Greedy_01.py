# Greedy_01
n = 1260
count = 0

coin = [500, 100, 50, 10]

for i in coin:
    count += n // i
    n %= i

print(count)

# 화폐의 종류를 K개라고 할 때 시간 복잡도 O(K)