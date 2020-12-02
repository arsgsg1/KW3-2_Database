import matplotlib.pyplot as plt
import numpy as np
import warnings
import matplotlib
import pymysql.cursors
import pandas as pd
import numpy
import dataframe_image as dfi

# DB 내 작품 정보 가져오기
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='3721',
    db='registration',
    charset='utf8')

curs = conn.cursor()
sql = "SELECT student_id, term, credit_hour, grade_average, major_grade_average, electives_grade_average FROM score where student_id = 2015722052 order by term"
curs.execute(sql)

result = curs.fetchall()
df_all=pd.DataFrame(result, columns=["학번", "학기", "이수학점", "평균평점", "전공평균평점", "교양평균평점"])

df_image = df_all.loc[:, ['학기', '이수학점', '평균평점', '전공평균평점', '교양평균평점']]
# 다른 방법
# df_sample = data[['성별코드', '신장(5Cm단위)', '체중(5Kg 단위)', '허리둘레', '흡연상태', '음주여부']]

dfi.export(df_image, './static/grade_table.png')

sql = "select round(avg(grade_average),2) from score group by term"
curs.execute(sql)

total_average = curs.fetchall()
print(total_average)

grade_list=[]
major_grade_list=[]
electives_grade_list=[]
total_grade_list=[]

i=0
for row in df_all.iterrows():
    grade_list.append([row[1][1],row[1][3]])
    major_grade_list.append([row[1][1],row[1][4]])
    electives_grade_list.append([row[1][1],row[1][5]])
    total_grade_list.append([row[1][1],total_average[i][0]])
    i+=1

df_grade_average=pd.DataFrame(grade_list, columns = ['학기' , '평균평점'])
df_major_grade_average=pd.DataFrame(major_grade_list, columns = ['학기' , '전공평균평점'])
df_electives_grade_average=pd.DataFrame(electives_grade_list, columns = ['학기' , '교양평균평점'])
df_total_grade_average=pd.DataFrame(total_grade_list, columns = ['학기' , '학교평균평점'])


conn.close()

# 한글 출력 설정
matplotlib.rcParams['axes.unicode_minus'] = False
plt.rcParams["font.family"] = 'Malgun Gothic'
# 경고문 출력 X
warnings.filterwarnings('ignore')
flg2 = plt.figure() # 차트 플롯 생성
chart = flg2.add_subplot(1, 1, 1) # 행, 열, 위치

label = ['2019-1', '2019-2', '2020-1', '2020-2']
x = numpy.arange(4)

# data 생성

total_data = df_total_grade_average.학교평균평점.tolist()



# 계단형 차트
#chart.plot(data1, label='2020년도 점수', drawstyle='default', color='thistle') # 선그래프로 출력
df_grade_average.평균평점.plot.bar(x,label='평균평점', width=-0.3, color='#ff9999',align='edge')    # bar(수직막대) - color에서 색깔 조정
df_major_grade_average.전공평균평점.plot.bar(x,label='전공평균평점', width=0.3, color='#ffc000',align='center')    # bar(수직막대) - color에서 색깔 조정
df_electives_grade_average.교양평균평점.plot.bar(x+0.3,label='교양평균평점', width=0.3, color='#8fd9b6',align='edge')    # bar(수직막대) - color에서 색깔 조정

# 선 스타일 차트
chart.plot(total_data, drawstyle='default',label='전체학생평균', color='#702946') # 평균 - color에서 색깔 조정


plt.xlabel('기간') # x축
plt.xticks(np.arange(0, 4), labels=['2019-1', '2019-2', '2020-1', '2020-2'], rotation=0, fontsize=12)

plt.ylabel('점수') # y축
plt.ylim([0, 4.5]) # Y축의 범위: [ymin, ymax]
#plt.axhline(y=47.71400000000001, color='purple', linewidth=1, label="전체 작품 점수 평균") # 일직선
plt.legend(loc='best') # 범례

#plt.show()
plt.savefig('./static/score.png') # 이미지 png로 저장