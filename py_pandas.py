# 요구 사항 : 딕셔너리 자료형의 데이터를 csv 형식의 파일로 저장하고, 반드시 저장된 파일을 읽어 출력하세요.
#             또한, 반드시 pandas 패키지를 이용해야 합니다.
# 요구 출력결과
# 	  음식	    놀이
# 0	  짜장면	그네
# 1	  만두	    물구나무

value = {'음식' : ['짜장면', '만두'],
         '놀이' : ['그네', '물구나무']}

import pandas as pd

df = pd.DataFrame(value)
df.to_csv('./food-and-play.csv')
df
