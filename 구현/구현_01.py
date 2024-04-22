# 구현_01
n = int(input())
plans = input().split()

x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
direction = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(direction)):
        if plan == direction[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시한다
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)

# 이동 횟수가 N번인 경우 시간 복잡도 O(N)