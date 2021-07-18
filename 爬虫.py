import json

import pandas as pd
import requests
from bs4 import BeautifulSoup


# 第一个爬虫:爬取一些东西返回列表
def crawl_page(url, job_href_list):
    # 向网页发送请求
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    # print(response.status_code)
    response.encoding = 'GBK'  # 解决后面解析网页是出现乱码的问题
    # 解析html文档
    soup = BeautifulSoup(response.text, 'lxml')
    lianjie = soup.find_all('script', {'type': 'text/javascript'})[2]
    engine_search_result = (json.loads(str(lianjie)[60:-9]))['engine_search_result']  # engine_search_result

    for x in engine_search_result:
        job_href_list.append(x['job_href'])
    # print(len(company_href_list))
    return job_href_list


def crawl_details_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    response.encoding = 'GBK'  # 解决后面解析网页是出现乱码的问题
    soup = BeautifulSoup(response.text, 'lxml')
    zhihwumingcheng = soup.find('h1').text
    # print("职务名称", zhihwumingcheng)
    msg = soup.find('p', class_='msg ltype').text  # [城市,工作年限,学历要求,人数,发布日期]
    msg = msg.split("|")
    chengshi = msg[0][:-2]
    gongzuonianxian = msg[1][2:-2]
    xueliyaoqiu = msg[2][2:-2]
    renshu = msg[3][2:-2]
    faburiqi = msg[4][2:-2]
    tHeader = soup.find('div', class_="tHeader tHjob")
    yuexinfanwei = tHeader.find('strong').text
    # print("月薪范围", yuexinfanwei)
    zhinengleibie = soup.find('a', class_='el tdn').text
    # print("职能类别", zhinengleibie)
    fuli = soup.find('div', class_='t1').text
    # print("福利", fuli.replace('\n', ''))
    gongsilianjie = soup.find('a', class_='catn').get('href')
    # print("公司链接", gongsilianjie)
    gongsimingcheng = soup.find('a', class_='catn').text
    # print("公司名称", gongsimingcheng)
    lianxifangshi = soup.find('div', class_='bmsg inbox').find('p', class_='fp').text
    # print("联系方式", lianxifangshi)
    gangweizhize = soup.find('div', class_='bmsg job_msg inbox').text.replace('\n', '')
    # print("岗位职责", gangweizhize)
    info = {
        "职务名称": zhihwumingcheng,
        "城市": chengshi,
        "工作年限": gongzuonianxian,
        "学历要求": xueliyaoqiu,
        "人数": renshu,
        "发布日期": faburiqi,
        "月薪范围": yuexinfanwei,
        "职能类别": zhinengleibie,
        "福利": fuli,
        "公司链接": gongsilianjie,
        "公司名称": gongsimingcheng,
        "联系方式": lianxifangshi,
        "岗位描述": gangweizhize
    }
    return info


infos = []

for i in range(401, 831):
    print("正在爬取第", i, "页")
    # 选择网站的页面
    url1 = "https://search.51job.com/list/000000,000000,0100,01%252c37%252c38%252c32%252c40,9,99,+,2,"
    url2 = str(i)
    url3 = ".html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
    url = url1 + url2 + url3

    job_href_list = []
    crawl_page(url, job_href_list)
    print("正在处理第", i, '页的50条详情信息')
    for url in job_href_list:
        # print("正在获取", url, "的详细信息")
        try:
            info = crawl_details_page(url)
            infos.append(info)
        except:
            print(url, '解析出错')
    print("第", i, '页爬取完毕')

# 导出infos到文件
pd.DataFrame(infos).to_csv("data/lx_infos.csv", encoding='utf-8')

import pandas as pd
import numpy as np

data = pd.read_csv('/home/aistudio/work/train.csv')
data.columns

data.head(3)

data = data[['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']]

data['Age'] = data['Age'].fillna(data['Age'].mean())

data.fillna(0, inplace=True)

data['Sex'] = [1 if x == 'male' else 0 for x in data.Sex]

data['p1'] = np.array(data['Pclass'] == 1).astype(np.int32)
data['p2'] = np.array(data['Pclass'] == 2).astype(np.int32)
data['p3'] = np.array(data['Pclass'] == 3).astype(np.int32)

del data['Pclass']

data.Embarked.unique()

data['e1'] = np.array(data['Embarked'] == 'S').astype(np.int32)
data['e2'] = np.array(data['Embarked'] == 'C').astype(np.int32)
data['e3'] = np.array(data['Embarked'] == 'Q').astype(np.int32)

del data['Embarked']

data.values.dtype

data.head(3)

data_train = data[['Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'p1', 'p2', 'p3', 'e1', 'e2', 'e3']].values

data_target = data['Survived'].values.reshape(len(data), 1)

np.shape(data_train), np.shape(data_target)

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(data_train, data_target, test_size=0.2)

x_train.shape, x_test.shape

from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier()

model.fit(x_train, y_train)

model.score(x_test, y_test)

model.score(x_train, y_train)


def m_score(depth):  # 单个参数
    model = DecisionTreeClassifier(max_depth=depth)
    model.fit(x_train, y_train)
    train_score = model.score(x_train, y_train)
    test_score = model.score(x_test, y_test)
    return train_score, test_score


depths = range(2, 15)
scores = [m_score(depth) for depth in depths]

scores

train_s = [s[0] for s in scores]

test_s = [s[1] for s in scores]

import matplotlib.pyplot as plt

plt.plot(depths, train_s)
plt.plot(depths, test_s)

plt.show()


def m_score(value):
    model = DecisionTreeClassifier(min_impurity_decrease=value)
    model.fit(x_train, y_train)
    train_score = model.score(x_train, y_train)
    test_score = model.score(x_test, y_test)
    return train_score, test_score


values = np.linspace(0, 0.5, 50)

scores = [m_score(value) for value in values]

train_s = [s[0] for s in scores]
test_s = [s[1] for s in scores]

best_index = np.argmax(test_s)

dest_score = test_s[best_index]

plt.plot(train_s)
plt.plot(test_s)

plt.show()

from sklearn.model_selection import GridSearchCV

values = np.linspace(0, 0.5, 50)
depths = range(2, 15)

param_grid = {'max_depth': depths, 'min_impurity_decrease': values}

model = GridSearchCV(DecisionTreeClassifier(), param_grid, cv=5)

model.fit(data_train, data_target)

model.best_params_

model.best_score_
