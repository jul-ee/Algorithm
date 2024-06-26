# 구현_03
location = input()
row = int(location[1])
column = int(ord(location[0])) - int(ord('a')) + 1

# 시계 방향으로 나이트가 이동할 수 있는 8가지 방향 정의
# (row, column)
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)