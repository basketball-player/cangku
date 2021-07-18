import pandas as pd

# 数据预处理包括
# '职务名称', 不处理
# '城市', 找到-并删之后的字符
# '工作年限', 剔除非法值 编码
# '学历要求', 剔除非法值 编码
# '人数', 非法值在剔除学历要求时已被提出
# '发布日期', 不处理
# '月薪范围', 分成三个字段 月薪上限、月薪下限、月薪均值
# '职能类别', 不处理
# '福利', 不处理
# '公司链接', 不处理
# '公司名称', 不处理
# '联系方式', 不处理
# '岗位描述' 不处理

data = pd.read_csv("data/test.csv", index_col=0)
data.reset_index(drop=True, inplace=True)
# 查看数据特征
print(data.columns)  # 查看列索引
print(data.index)  # 查看行索引
print(data.shape)  # 查看行数列数

# 过滤缺失值
print("过滤缺失值之前有", data.shape[0], "条数据")
data.dropna(how='any', inplace=True)  # 如果某行数据中有某一个列属性值空 则删除改行 并覆盖原来的DataFrame
print("过滤缺失值之后有", data.shape[0], "条数据")

# 处理城市
chengshilist = []
for cs in data["城市"]:
    fenge = cs.split('-')
    chengshilist.append(fenge[0])
data["城市"] = chengshilist
# print(data["城市"].value_counts())


# 处理工作年限
# print(data["工作年限"].value_counts())
# 列举出工作年限这一列合法的取值
keys = ["无需经验", "在校生/应届生", "1年经验", "2年经验", "3-4年经验", "5-7年经验", "8-9年经验", "10年以上经验"]
# 过滤掉工作年限的非法值
data = data[data["工作年限"].isin(["无需经验", "在校生/应届生", "1年经验", "2年经验", "3-4年经验", "5-7年经验", "8-9年经验", "10年以上经验"])]
# print(data["工作年限"].value_counts())
# 对工作年限进行编码
values = [0, 1, 2, 3, 4, 5, 6, 7]
code = dict(zip(keys, values))
print(code)
data.replace({"工作年限": code}, inplace=True)
# print(data["工作年限"].value_counts())
print("处理工作年限后有", data.shape[0], "条数据")

# 处理学历要求
# print(data["学历要求"].value_counts())
# 列举出学历要求这一列合法的取值
keys = ["初中", "高中", "中专", "大专", "本科", "硕士", "博士"]
# 删除学历要求的非法取值的行
data = data[data["学历要求"].isin(["初中", "高中", "中专", "大专", "本科", "硕士", "博士"])]
# print(data["学历要求"].value_counts())
# 对学历要求进行编码
values = [0, 1, 2, 3, 4, 5, 6]
code = dict(zip(keys, values))
print(code)
data.replace({"学历要求": code}, inplace=True)
# print(data["学历要求"].unique())

data.dropna(how='any', inplace=True)  # 如果某行数据中有某一个列属性值空 则删除改行 并覆盖原来的DataFrame
print("处理学历要求后有", data.shape[0], "条数据")

renshu_list = []
a = 0  # 用来处理异常值'若干',用其上一个值来替代
for k in data['人数']:
    if k[1:-1] == '若干':
        renshu_list.append(a)
    else:
        a = int(k[1:-1])  # 储存非'若干'的值的数据，用来替代'若干'
        renshu_list.append(int(k[1:-1]))
# print(renshu_list)
data["人数"] = renshu_list
data.dropna(how='any', inplace=True)  # 如果某行数据中有某一个列属性值空 则删除改行 并覆盖原来的DataFrame
print("处理人数后有", data.shape[0], "条数据")

yuxinmin_list = []  # 月薪下限
yuxinmax_list = []  # 月薪上限
yuxinmean_list = []  # 月薪均值

# '月薪范围'有
# a-b万/年   'k[0:-3]'提取'a-b','.split("-")[0]'提取'a','.split("-")[1]'提取'b'
# a-b万/月   'k[0:-3]'提取'a-b','.split("-")[0]'提取'a','.split("-")[1]'提取'b'
# a-b千/月   'k[0:-3]'提取'a-b','.split("-")[0]'提取'a','.split("-")[1]'提取'b'
# a元/天      'k[0:-3]'提取'a'
# a元/小时    'k[0:-4]'提取'a'
# a万以上/年  'k[0:-5]'提取'a'
# a万以上/月  'k[0:-5]'提取'a'
# a千以下/月  'k[0:-5]'提取'a'

for k in data['月薪范围']:
    if k[-1] == '年':
        if k[-3] == '万':
            yuxinmin_list.append(float(k[0:-3].split("-")[0]) / 1.2)
            yuxinmax_list.append(float(k[0:-3].split("-")[1]) / 1.2)
            yuxinmean_list.append((float(k[0:-3].split("-")[0]) + float(k[0:-3].split("-")[1])) / 2.4)
        elif k[-5] == '万':
            yuxinmin_list.append(float(k[0:-5]) / 1.2)
            yuxinmax_list.append(float(k[0:-5]) / 1.2)
            yuxinmean_list.append(float(k[0:-5]) / 1.2)
    elif k[-1] == '月':
        if k[-3] == '万':
            yuxinmin_list.append(float(k[0:-3].split("-")[0]) * 10)
            yuxinmax_list.append(float(k[0:-3].split("-")[1]) * 10)
            yuxinmean_list.append((float(k[0:-3].split("-")[0]) + float(k[0:-3].split("-")[1])) * 5)
        elif k[-3] == '千':
            yuxinmin_list.append(float(k[0:-3].split("-")[0]))
            yuxinmax_list.append(float(k[0:-3].split("-")[1]))
            yuxinmean_list.append((float(k[0:-3].split("-")[0]) + float(k[0:-3].split("-")[1])) / 2)
        elif k[-5] == '万':
            yuxinmin_list.append(float(k[0:-5]) * 10)
            yuxinmax_list.append(float(k[0:-5]) * 10)
            yuxinmean_list.append(float(k[0:-5]) * 10)
        elif k[-5] == '千':
            yuxinmin_list.append(float(k[0:-5]))
            yuxinmax_list.append(float(k[0:-5]))
            yuxinmean_list.append(float(k[0:-5]))
    elif k[-1] == '天':
        if k[-3] == '元':
            yuxinmin_list.append(float(k[0:-3]) * 30 / 1000)
            yuxinmax_list.append(float(k[0:-3]) * 30 / 1000)
            yuxinmean_list.append(float(k[0:-3]) * 30 / 1000)
    elif k[-2:] == '小时':
        if k[-4] == '元':
            yuxinmin_list.append(float(k[0:-4]) * 30 * 24 / 1000)
            yuxinmax_list.append(float(k[0:-4]) * 30 * 24 / 1000)
            yuxinmean_list.append(float(k[0:-4]) * 30 * 24 / 1000)
data['月薪下限'] = yuxinmin_list
data['月薪上限'] = yuxinmax_list
data['月薪均值'] = yuxinmean_list
data.dropna(how='any', inplace=True)  # 如果某行数据中有某一个列属性值空 则删除改行 并覆盖原来的DataFrame
print("处理月薪后有", data.shape[0], "条数据")

data.drop_duplicates()
print("去除重复值后有", data.shape[0], "条数据")

# print(data["职能类别"].value_counts())
# print(data[data["职能类别"] == "研究生"].values)


# 导出处理后的数据到csv文件
data.to_csv("chulihou.csv")
