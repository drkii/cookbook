## 0x scraping
```Python
#requestというライブラリを使う
import requests
# 取得したいURLを書きます
url = "http://docs.pyq.jp/_static/assets/scraping/test1.html"

# HTTPリクエストを送信してHTMLを取得します
# 日本語対応するためのエンコーディング
# encoding プロパティーは、サーバーから返されるレスポンスの文字エンコーディングです。この文字エンコーディングにしたがって、コンテンツを変換してくれます。
# apparent_encoding はサーバーから返される 文字エンコーディング が不明な場合にコンテンツの中身をチェックした上で適切な 文字エンコーディングを教えてくれます。これを respones.encoding にセットすることで、極力文字化けなどが起こらないようにコンテンツを取得できます。
response = requests.get(url)
response.encoding = response.apparent_encoding
# 取得したHTMLを表示します
print(response.text)

#Ans
# <!DOCTYPE html>
# <html lang="ja">
#   <head>
#     <meta charset="utf-8">
#     <title>最初のHTML</title>
#   </head>
#   <body>
#     <h1>最初のHTML</h1>
#     <p>スクレイピングテスト</p>
#   </body>
# </html>
---------
# CSVのURL
import requests
# 取得したいCSVのURLを書きます
url = "http://docs.pyq.jp/_static/assets/scraping/test2.csv"

# HTTPリクエストを送信してCSVを取得します
response = requests.get(url)
response.encoding = response.apparent_encoding
# 取得したCSVを表示します
print(response.text)


---------
# 複数のURLから（必ず１秒開けましょう）
import time
import requests

# 取得したいURL書きましょう
url_html = "http://docs.pyq.jp/_static/assets/scraping/test1.html"
url_csv = "http://docs.pyq.jp/_static/assets/scraping/test2.csv"

# HTMLの取得と表示
response = requests.get(url_html)
response.encoding = response.apparent_encoding

print("HTMLの取得と表示 ----")
print(response.text)

# 1秒スリープ
time.sleep(1)
# CSVの取得と表示
response = requests.get(url_csv)
response.encoding = response.apparent_encoding

print("CSVの取得と表示 ----")
print(response.text)

---------
#ファイルへ書き出し(ensyu1.html, ensyu1.csv)
import time
import requests

url_html = "http://docs.pyq.jp/_static/assets/scraping/ensyu1.html"
url_csv = "http://docs.pyq.jp/_static/assets/scraping/ensyu1.csv"

response = requests.get(url_html)
response.encoding = response.apparent_encoding
ensyu_html = response.text

time.sleep(1)
response = requests.get(url_csv)
response.encoding = response.apparent_encoding
ensyu_csv = response.text

with open('ensyu1.html', mode='w', encoding='utf-8') as fp:
    fp.write(ensyu_html)
with open('ensyu1.csv', mode='w', encoding='utf-8') as fp:
    fp.write(ensyu_csv)

```
