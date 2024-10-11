# 요구 사항 : 제시된 리스트 자료형을 아무 파일로 저장하고, 반드시 저장된 파일을 읽고 결과를 출력하세요.
# 요구 출력결과
# [1, 2, 3, 4, 5]
import pickle

value = [1, 2, 3, 4, 5]

with open('assignment_11.pkl', 'wb') as file:
    pickle.dump(value, file)

with open('assignment_11.pkl', 'rb') as file:
    result = pickle.load(file)

print(result)
