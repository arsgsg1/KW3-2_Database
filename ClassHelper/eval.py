def eval_graph(subject_id):
    import matplotlib.pyplot as plt
    import numpy as np
    import warnings
    import matplotlib
    import pymysql.cursors
    import pandas as pd
    import numpy

    # DB 내 작품 정보 가져오기
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='3721',
        db='registration',
        charset='utf8')

    curs = conn.cursor()
    sql = "SELECT * FROM subject_eval where subject_id = %s and term='2020-2'"
    curs.execute(sql,(subject_id,))

    result = curs.fetchall()

    verygood, good, soso, bad, verybad=0,0,0,0,0
    for i in result:
        if i[4]>=80:
            verygood+=1
        elif i[4]>=60 and i[4]<80:
            good+=1
        elif i[4]>=40 and i[4]<60:
            soso+=1
        elif i[4]>=20 and i[4]<40:
            bad+=1
        else:
            verybad+=1

    ratio = [verygood/len(result), good/len(result), soso/len(result), bad/len(result), verybad/len(result)]    

    labels = ['Very good', 'Good', 'SoSo', 'Bad', 'Very Bad']

    explode = [0.15, 0.05, 0.05,0.05, 0.05]
    colors = ['#ff9999', '#ffc000', '#8fd9b6', '#d395d0', '#5e7e9b']
    wedgeprops={'width': 0.7, 'edgecolor': 'w', 'linewidth': 2}

    plt.rcParams["font.family"] = 'Malgun Gothic'
    plt.pie(ratio, labels=labels, autopct='%.1f%%', startangle=90, counterclock=False, explode=explode, shadow=True, colors=colors, wedgeprops=wedgeprops)
    #plt.show()
    plt.savefig('./static/eval.jpeg') # 이미지 png로 저장