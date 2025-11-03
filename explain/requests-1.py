import requests

#对网站发起请求
x= requests.get("https://anuyoah.com");

#获取返回代码-响应头-内容
print(x.status_code);
print(x.headers);
# print(x.content);

