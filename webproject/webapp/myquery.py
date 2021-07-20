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
        WHERE WY=0 AND JC NOT LIKE '%其他%' AND city='{}'
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
    return top_jobs


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
def query5(cursor, city, top_job_list,n):
    rows = []
    try:
        for i in range(n):
            row = []
            sql = '''
            SELECT SUM(number) AS TN,AVG(MSM) AS MMSM 
            FROM fulltable WHERE city='{}' AND JC='{}' 
            '''.format(city,top_job_list[i])
            cursor.execute(sql)
            result_list1 = dict_fetch_all(cursor)
            result_list1[0]["MMSM"] = round(result_list1[0]["MMSM"], 2)
            row.append(result_list1[0])
            sql = '''
            SELECT SUM(number) AS TN,AVG(MSM) AS MMSM 
            FROM fulltable WHERE city='{}' AND JC='{}' AND AR=4 
            '''.format(city,top_job_list[i])
            cursor.execute(sql)
            result_list2 = dict_fetch_all(cursor)
            row.append(result_list2[0])
            sql = '''
            SELECT SUM(number) AS TN,AVG(MSM) AS MMSM 
            FROM fulltable WHERE city='{}' AND JC='{}' AND WY=1 
            '''.format(city,top_job_list[i])
            cursor.execute(sql)
            result_list3 = dict_fetch_all(cursor)
            row.append(result_list3[0])
            row.append({"rate":round(100*result_list3[0]["TN"]/result_list1[0]["TN"], 3)})
            # print(row)
            rows.append(row)
    except:
        rows.append([])
    return rows



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
    wc.create_wordcloud(results[0]["keywords"], "static/wc/北京_软件测试工程师")
