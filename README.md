# python-get-domain-information

## 本代码原理  使用第三方库获取域名信息  把域名信息保存到MySql

## 环境准备：
- 安装python的第三库 python-whois `pip3 install python-whois`
- 安装pymysql  `pip3 install pymysql`

## 实现原理
- MySQL连接
```python
db = pymysql.connect(host='137.220.133.133', user='root', password='jacky1980!@#$', database='query_domain', charset='utf8')
cursor = db.cursor()
```
- 因域名太多，所以实现批量 读取域名文本
```python
with open('profile.txt','r',encoding='utf-8')as f:
    data = f.readlines()
```

## 声明
本次代码只是简易版本，没有加到代理，没有使用多线程，仅供学习参考，有好的意见欢迎留言
