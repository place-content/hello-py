# 요구 사항 : 숫자만을 원소로 하는 리스트 자료형 입력받아 최대값을 찾는 프로그램을 완성하세요.
#             단, 반드시 max() 함수를 사용해야 합니다.
# 요구 출력결과
# 9

value = [1, 4, 6, 7, 3, 2, 9]
result = [x for x in value if x > 0]
print(max(result))
