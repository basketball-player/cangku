from django.db import connection
from django.shortcuts import render
from webapp import wc

# Create your views here.
def index_page(request):
    a = 1
    list1 = ['1','2']
    data = {'cs':['bj','sh']}
    datas = {'cs':['bj','sh'],
            'rs':['1','2']}
    data2 = [
        [11,12],
        [21,22]
    ]
    return render(request, "scratch_1.html", {'a':a,'list1':list1,'data':data,'datas':datas,"data2":data2})


def dictfetchall(cursor):
    desc = cursor.description
    return [dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()]



def city_page(request):
    cursor = connection.cursor()
    # 计算出某城市的月薪中位数 及其排名
    # 计算出某城市的岗位需求量 及其排名
    # 计算出某城市的应届生需求量 及其排名
    sql = '''
    SELECT
        city_infos.city, MdS, MSrnk, TD, TDrnk, ND, NDrnk
    FROM
        city_rnk,
        city_infos
    WHERE
        city_rnk.city = city_infos.city
    '''
    cursor.execute(sql)
    results = dictfetchall(cursor)
    for row in results:
        if row['city'] == "北京":
            # print(row)
            MS = row["MdS"]  # 月薪中位数
            MSrnk = row["MSrnk"]  # 月薪中位数排名
            TD = row["TD"]  # 岗位总需求量
            TDrnk = row["TDrnk"]  # 岗位总需求量排名
            ND = row["ND"]  # 应届生需求量
            NDrnk = row["NDrnk"]  # 应届生需求量排名
            # print(MS, MSrnk, TD, TDrnk, ND, NDrnk)
            break

    # 计算出某城市的应届生需求量最大的n个岗位
    # sql = '''
    # select city,job, sum(number) as ND
    # from fulltable
    # where workingyears=0 and job not like'%其他%'
    # group by city,job
    # order by ND desc
    # '''
    city = "北京"
    sql = '''
    SELECT city,JC,sum( number ) AS ND 
    FROM fulltable 
    WHERE WY = 0 AND JC NOT LIKE '%其他%'  AND city = '{}' 
    GROUP BY city,JC 
    ORDER BY ND DESC
    '''.format(city)
    cursor.execute(sql)
    results = dictfetchall(cursor)
    # print(results)
    i = 0
    n = 80
    top_job_list = []  # 总需求量最大的n个岗位名称
    for row in results:
        # print(row)
        i += 1
        top_job_list.append(row["JC"])
        if i >= n:
            break
    # print(top_job_list)
    top1 = top_job_list[0]  # 需求量最大的岗位1
    top2 = top_job_list[1]  # 需求量最大的岗位2
    top3 = top_job_list[2]  # 需求量最大的岗位3
    top4 = top_job_list[3]  # 需求量最大的岗位4
    top5 = top_job_list[4]  # 需求量最大的岗位5
    # 计算出Top5岗位的(月薪/工作年限/学历要求){}
    sql = '''
    SELECT JC, MSM, WY,AR 
    FROM fulltable 
    WHERE JC = '{}' AND city='{}'
    '''.format(top_job_list[0], city)
    cursor.execute(sql)
    results = dictfetchall(cursor)
    MS_list = []
    WY_list = []
    AR_list = []
    for row in results:
        # print(row)
        MS_list.append(row["MSM"])
        WY_list.append(row["WY"])
        AR_list.append(row["AR"])

    # print(MS_list)
    # print(WY_list)
    # print(AR_list)

    # Top80岗位的 岗位需求量应届生需求量月薪中位数全国排名本科岗位占比

    sql = '''

    '''
    data = [[11, 12, 13, 14, 15, 16, 17], [21, 22, 23, 24, 25, 26]]
    # data = [ ["world", "6562695", "121413", "386788", "4929", "3161280", "3014627", "54202", "0"],
    # ["usa", "1901783", "20578", "109142", "1083", "688670", "1103971", "16939", "19096671"],
    # ["brazil", "583980", "27312", "32547", "1269", "266132", "285301", "8318", "930013"],
    # ]

    # 动态计算岗位词云需要的词频统计列表
    sql = '''
    select group_concat(JD) as str
    from fulltable
    where city = '{}' and JC = '{}'
    '''.format("北京","软件测试工程师")
    cursor.execute(sql)
    results = dictfetchall(cursor)
    # print(results[0]["str"])
    wc.create_wordcloud(results[0]["str"],"static/wc/北京_软件测试工程师")

    return render(request, "city.html", {
        "MS": MS, "MSrnk": MSrnk, "TD": TD, "TDrnk": TDrnk, "ND": ND, "NDrnk": NDrnk,
        "top1": top1, "top2": top2, "top3": top3, "top4": top4, "top5": top5,
        "MS_list": MS_list, "WY_list": WY_list, "AR_list": AR_list, "data": data
    })

# 用户在打开首页 点击城市之后就开始计算这个城市的相关数据 前6个数字直接在视图中查询
# 6个数字+岗位列表+岗位1的具体数据(月薪/工作年限/学历)+前80个岗位对应的表


# 准备工作 服务器启动之前的事情
# 提前把FullTabel建好
# 制作各城市的宏观统计数据视图

# 打开首页点击城市之后的事情
# 计算这个城市的数据 6个数字+Top5岗位名称+岗位1的具体数据序列(月薪/工作年限/学历)+前80个岗位对应的表

# 点击岗位选择按钮 异步加载各个岗位的数据
# 用户点击第二板块的几个岗位按钮之后 异步加载获取数据绘制对应的折线图
# 用户点击第三板块的生成词云按钮之后 异步加载获取数据绘制对应的词云
