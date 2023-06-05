# python-get-domain-information

## 本代码原理  使用第三方库获取域名信息  把域名信息保存到MySql

## 环境准备：
- 安装python的第三库 python-whois `pip3 install python-whois`
- 安装pymysql  `pip3 install pymysql`

## 实现原理
- MySQL连接
```python
db = pymysql.connect(host='localhost', user='root', password='password', database='query_domain', charset='utf8')
cursor = db.cursor()
```
- 因域名太多，所以实现批量 读取域名文本
```python
with open('profile.txt','r',encoding='utf-8')as f:
    data = f.readlines()
```
- 代码核心 使用for循环遍历刚才读取出来的域名  在使用python-whois 进行请求  获取请求使用字典储存 最后把字典存进MySQL
```python
or i in data:
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

```
- 关闭MySQL连接
```python
db.close()
```

## 声明
本次代码只是简易版本，没有加到代理，没有使用多线程，仅供学习参考，有好的意见欢迎留言
