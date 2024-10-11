# 요구 사항 : <문제-11>에서 저장된 파일을 읽어 모든 원소에 +10을 한 후 다른 파일명으로 저장하세요. 그런 후, 반드시 저장된 파일을 읽고 결과를 출력하세요.
# 요구 출력결과
# [11, 12, 13, 14, 15]
import pickle # 위에 설정해서 선언 안해줘도 되지만 혹시 몰라 선언

value = [1, 2, 3, 4, 5]

with open('assignment_11.pkl', 'rb') as file:
    v = pickle.load(file)

new_v = [x + 10 for x in v]


with open('assignment_12.pkl', 'wb') as file:
    pickle.dump(new_v, file)

with open('assignment_12.pkl', 'rb') as file:
    result = pickle.load(file)

print(result)