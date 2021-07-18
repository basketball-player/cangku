import json

import requests
from bs4 import BeautifulSoup

# Create Table (城市 公司名称 公司链接 联系方式);
# companysize = ["少于50:[公司1,公司2,...],"50-100人":[公司3,公司4,...],,,]

keys = ['北京', '上海', '广州', '深圳', '武汉', '西安', '杭州',
        '南京', '成都', '重庆', '东莞', '大连', '沈阳', '苏州',
        '昆明', '长沙', '合肥', '宁波', '郑州', '天津', '青岛',
        '济南', '哈尔滨', '长春', '福州', '珠三角']
values = ['010000', '020000', '030200', '040000', '180200', '200200', '080200', '070200', '090200', '060000',
          '030800', '230300', '230200', '070300', '250200', '190200', '150200', '080300', '170200', '050000',
          '120300', '120200', '220200', '240200', '110200',
          '01']
chengshibianhao = dict(zip(keys, values))
guimobianhao = {"少于50人": 1, "50-150人": 2, "150-500人": 3, "500-100人": 4,
                "1000-1500人": 5, "5000-10000人": 6, "10000人以上": 7}
yemianshu = {}
page = []


# print(guimo[3])


def crawl_company(city_name, gongsiguimo):
    url1 = "https://search.51job.com/list/"
    url2 = chengshibianhao[city_name]
    url3 = ",000000,0000,00,9,99,+,2,"
    url4 = '1'
    url5 = ".html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize="
    url6 = guimobianhao[gongsiguimo]
    url7 = "&ord_field=0&dibiaoid=0&line=&welfare="
    for url4 in range(yemianshu[city_name]):
        url = url1 + url2 + url3 + str(url4) + url5
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        script = soup.find_all('script', {'type': 'text/javascript'})[2]
        engine_search_result = (json.loads(str(script)[60:-9]))['engine_search_result']  # engine_search_result

        for x in engine_search_result:
            gongsimingcheng = x["company_name"]
            gongsixingzhi = x["companytype_text"]
            gongsiguimo = gongsiguimo
            info = {
                "公司名称": gongsimingcheng,
                "公司性质": gongsixingzhi,
                "公司规模": gongsiguimo
            }
            gongsi.append(info)


gongsi = []
# crawl_company('北京','少于50人')
print("爬取完毕")
print(len(gongsi))


def crawl(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    hhh = soup.find('div', class_='in')
    print(hhh)


url = "https://jobs.51job.com/all/co2370244.html"
crawl(url)
