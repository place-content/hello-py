# 요구 사항 : 이메일 주소를 분해하여 계정과 도메인 리스트를 만드는 코드를 완성하세요. 단, 반드시 리스트 컴프리헨션으로 만드세요.
# 요구 출력결과
# ['a', 'b', 'c']
# ['naver.com', 'google.co.kr', 'daum.net']
data = ['a@naver.com', 'b@google.co.kr', 'c@daum.net']
id_list = [x.split("@")[0] for x in data]
domain_list = [x.split("@")[1] for x in data]

print(id_list)
print(domain_list)