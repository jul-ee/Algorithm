n = int(input())

count = 0

for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            # 매 시각을 문자열로 자료형으로 변환
            # '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)