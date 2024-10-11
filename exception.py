# 요구 사항 : 다음 명령을 실행하면 오류가 발생됩니다. 반드시 오류를 예외처리하여 "완성"이 출력되도록 하세요.
# 요구 출력결과
# 완성

try:
    for i in range(sim):
        v = float(i)
except NameError:
    print('완성')

