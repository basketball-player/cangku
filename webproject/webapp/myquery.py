from webapp import wc


# 返回字典列表
def dict_fetch_all(cursor):
    desc = cursor.description
    return [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]


# 1.计算出某城市的月薪中位数及其排名/岗位需求量及其排名/应届生需求量及其排名
def query1(cursor, city):
    sql = '''
        SELECT city_infos.city, MdS, MSrnk, TD, TDrnk, ND, NDrnk
        FROM city_rnk, city_infos
        WHERE city_rnk.city = city_infos.city AND city_infos.city='{}'
    '''.format(city)
    cursor.execute(sql)
    result_list = dict_fetch_all(cursor)
    result = result_list[0]
    MdS, MSrnk = result["MdS"], result["MSrnk"]  # 月薪中位数/排名
    TD, TDrnk = result["TD"], result["TDrnk"]  # 岗位总需求量/排名
    ND, NDrnk = result["ND"], result["NDrnk"]  # 应届生需求量/排名
    # print(MdS, MSrnk, TD, TDrnk, ND, NDrnk)
    return MdS, MSrnk, TD, TDrnk, ND, NDrnk


# 2.计算出某城市的应届生需求量最大的n个岗位 返回列表
def query2(cursor, city, n=5):
    sql = '''
        SELECT city, JC, sum(number) AS ND 
        FROM fulltable 
        WHERE WY=1 AND JC NOT LIKE '%其他%' AND city='{}'
        GROUP BY city, JC
        ORDER BY ND DESC
    '''.format(city)
    cursor.execute(sql)
    result_list = dict_fetch_all(cursor)
    top_jobs = []
    try:
        for i in range(n):
            top_jobs.append(result_list[i]["JC"])
    except:
        pass
    return len(top_jobs), top_jobs


# 3.计算出Top5岗位的 月薪与学历要求的关系
def query3(cursor, city, top_job_list, n=5):
    values = []
    for i in range(n):
        sql = '''
            SELECT JC, avg(MSM), AR 
            FROM fulltable 
            WHERE JC = '{}' AND city='{}'
            group by AR
        '''.format(top_job_list[i], city)
        cursor.execute(sql)
        result_list = dict_fetch_all(cursor)
        # print(result_list)
        AR_MSM_list = [0, 0, 0, 0, 0, 0, 0]
        for result in result_list:
            AR_MSM_list[result["AR"]] = result["avg(MSM)"]
        # print(AR_MSM_list)
        values.append(AR_MSM_list)
    return values


# 4.计算出Top5岗位的 月薪与工作年限的关系
def query4(cursor, city, top_job_list, n=5):
    values = []
    for i in range(n):
        sql = '''
            SELECT JC, avg(MSM), WY 
            FROM fulltable 
            WHERE JC = '{}' AND city='{}'
            group by WY
        '''.format(top_job_list[i], city)
        cursor.execute(sql)
        result_list = dict_fetch_all(cursor)
        # print(result_list)
        WY_MSM_list = [0, 0, 0, 0, 0, 0, 0, 0]
        for result in result_list:
            WY_MSM_list[result["WY"]] = result["avg(MSM)"]
        # print(AR_MSM_list)
        values.append(WY_MSM_list)
    return values


# 5.计算某城市应届生需求量最大的前80个岗位的详细信息
def query5(cursor, city, top_job_list):
    sql = '''
        SELECT JC, SUM(number) AS TN,AVG(MSM) AS MMSM 
        FROM fulltable WHERE city='{}' AND JC in {} AND AR=4
        GROUP BY JC
    '''.format(city, top_job_list).replace('[', '(').replace(']', ')')
    cursor.execute(sql)
    result_list1 = cursor.fetchall()

    sql = '''
            SELECT SUM(number) AS TN
            FROM fulltable WHERE city='{}' AND JC in {} AND WY=1
            GROUP BY JC
        '''.format(city, top_job_list).replace('[', '(').replace(']', ')')
    cursor.execute(sql)
    result_list2 = cursor.fetchall()
    # print(result_list2)

    sql = '''
            SELECT SUM(number) AS TN
            FROM fulltable WHERE city='{}' AND JC in {}
            GROUP BY JC
    '''.format(city, top_job_list).replace('[', '(').replace(']', ')')
    cursor.execute(sql)
    result_list3 = cursor.fetchall()
    # print(result_list3)

    # 合并结果
    result = []

    for i in range(len(top_job_list)):
        try:
            i1 = result_list1[i][0]            # 岗位名称
            i2 = result_list1[i][1]            # 岗位需求量
            i3 = round(result_list1[i][2], 2)  # 月薪水平
            i4 = result_list2[i][0]            # 应届生需求量
            i5 = result_list3[i][0]            # 本科生需求量
            i6 = round(i5 / i2, 3)             # 本科岗位占比
            result.append([i1, i2, i3, i4, i5, i6])
            # print([i1, i2, i3, i4, i5, i6])
        except:
            pass

    # print(len(result))
    return len(result), result


# 6. 计算生成词云
def query6(cursor, city, job):
    sql = '''
    SELECT group_concat(JD) AS keywords
    FROM fulltable 
    WHERE city = '{}' AND JC = '{}'
    '''.format(city, job)
    cursor.execute(sql)
    results = dict_fetch_all(cursor)
    # print(results[0]["keywords"])
    wc.create_wordcloud(results[0]["keywords"], "static/wc/" + city + "_" + job)
