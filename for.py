# 요구 사항 : 이메일 주소를 분해하여 계정과 도메인 리스트를 만드는 코드를 완성하세요.
# 요구 출력결과
# ['a', 'b', 'c']
# ['naver.com', 'google.co.kr', 'daum.net']
def get_data(x):
    id_value = x.split("@")[0]
    domain_value = x.split("@")[1]
    return id_value, domain_value

data = ['a@naver.com', 'b@google.co.kr', 'c@daum.net']
id_list = []
domain_list = []
for x in data:
    id_, domain_ = get_data(x)
    id_list.append(id_)
    domain_list.append(domain_)

print(id_list)
print(domain_list)