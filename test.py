# coding: utf-8
import requests
import pandas as pd
import json
url = "https://api.cnyes.com/media/api/v1/newslist/category/headline" # 新聞連結 # 連結問號前面是url，後面是參數
payload = {"page":2, 
           "limit":30, 
           "isCategoryHeadline":1, 
           "startAt":1752645083, 
           "endAt":1753509083} # 參數
res = requests.get(url, params = payload) # 連線鉅亨網
jd = json.loads(res.text) # 解析json轉成dict
df = pd.DataFrame(jd['items']['data']) # 取出新聞資料
df = df[['newsId', 'title', 'summary']] # 取出特定欄位
df['link'] = df['newsId'].apply(lambda x: 'https://m.cnyes.com/news/id/' + str(x)) # 建立連結
df.to_csv('news.csv', encoding='utf-8-sig')
print(df)

