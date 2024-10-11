# 요구 사항 : 숫자만을 원소로 하는 리스트 자료형 입력받아 최대값을 찾는 프로그램을 완성하세요.
#             단, 반드시 IF문을 사용해야 합니다.
# 요구 출력결과
# 9

value = [1, 4, 6, 7, 3, 2, 9]
result = 0
for x in value:
    if result < x:
        result = x


print(result)
