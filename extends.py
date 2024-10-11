# 요구 사항 : <문제-8>에서 완성한 my_class 를 상속받아 최소값이 찾아내는 함수를 추가하세요. 반드시 상속받아 함수를 추가해야 합니다.
# 요구 출력결과
# 1
# (단, 이미 my_class가 선언되어있음을 가정하고 코드를 작성한다.)

value = [1, 4, 6, 7, 3, 2, 9]

class classes(my_class):
    def get_max(self, data):
        r = 0
        for x in data:
            if r > x:
                r = data
        return r

m = classes()
result = m.get_max(value)
print(result)