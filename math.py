# 요구 사항 : 숫자만을 원소로 하는 두 개의 리스트 자료형 입력받아 사칙연산 결과를 리턴하는 함수를 만드세요.
# 요구 출력결과
# 2 + 5 = 7
# 2 - 5 = -3
# 2 * 5 = 10
# 2 / 5 = 0.4
# 9 + 3 = 12
# 9 - 3 = 6
# 9 * 3 = 27
# 9 / 3 = 3

def abcd(x, y):
    return x+y, x-y, x*y, x/y

value1 = [2, 9]
value2 = [5, 3]
for v1 in value1:
    for v2 in value2:
        r1, r2, r3, r4 = abcd(v1, v2)
        print(f"{v1} + {v2} = {r1}")
        print(f"{v1} - {v2} = {r2}")
        print(f"{v1} * {v2} = {r3}")
        print(f"{v1} / {v2} = {round(r4, 1)}")
