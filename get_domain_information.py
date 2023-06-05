# -*- coding: utf-8 -*-

# @Time ： 2023/5/31 14:46
# @Auth ： Ly
# @File ：get_domain_information.py
# @IDE ：PyCharm
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  #改变标准输出的默认编码
import whois
import openpyxl
import pymysql


db = pymysql.connect(host='localhost', user='root', password='password', database='query_domain', charset='utf8')
cursor = db.cursor()

with open('profile.txt','r',encoding='utf-8')as f:
    data = f.readlines()

for i in data:
    try:

        item = {}
        links = i.strip('\n').replace('https://','').split('/')[0]


        domain =links
        w = whois.whois(domain)

        country = w.get("country")
        state = w.get("state")
        domain_name = w.get("domain_name")
        item['profile_links'] = i.strip('\n')
        if country is None:
            item['country'] = ''
        else:
            item['country'] = country

        if state is None:
            item['area'] = ''
        else:
            item['area'] = state


        if domain_name is None:
            item['domain_US'] = ''
            item['domain_ZH'] = ''
        elif isinstance(domain_name, str):
            item['domain_US'] = domain_name
            client = Translate()
            text = client.translate(item['domain_US'])
            item['domain_ZH'] = text.translatedText
        else:
            item['domain_US'] = domain_name[0]
            client = Translate()
            text = client.translate(item['domain_US'])
            item['domain_ZH'] = text.translatedText

        print(item)

        sql = "INSERT INTO domain_copy (country, area, domain_US, domain_ZH, profile_links) VALUES (%s, %s, %s, %s, %s)"
        val = (item['country'], item['area'], item['domain_US'], item['domain_ZH'], item['profile_links'])
        cursor.execute(sql, val)
        db.commit()

    except Exception as e:
        print('报错',e)


db.close()
