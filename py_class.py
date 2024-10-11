# 요구 사항 : 숫자만을 원소로 하는 리스트 자료형 입력받아 최대값을 찾는 프로그램을 완성하세요.
#             단, 반드시 클래스를 생성하여야 합니다.
# 요구 출력결과
# 9

value = [1, 4, 6, 7, 3, 2, 9]

class my_class:
    def get_max(self, data):
        r = 0
        for x in data:
            if r < x:
                r = x
        return r

m = my_class()
result = m.get_max(value)
print(result)
