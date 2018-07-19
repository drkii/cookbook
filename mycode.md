
# Python Cookbook

## 01. 入力を扱う
### スペース区切りで入力される文字列、数値をリストにする
```python
#文字列
words = [i for i in input().split()]
---------
#数値
numbers = [int(i) for i in input().split()]
```

### 標準入力される文字列を繰り返し出力する
```python
#標準入力値が5文字のPAIZA
t = input()
for i in t:
    print(i)
# 答え：
# P
# A
# I
# Z
# A
---------
#標準入力値が5文字のPAIZA
t = input()
for i in t:
    print(t)
# 答え：
# PAIZA
# PAIZA
# PAIZA
# PAIZA
# PAIZA

```

### 標準入力される文字列の数を若い順に取る
```python
#標準入力値が5文字のPAIZA
t = input()
l = int(len(t))
for i in range(l):
    print(i)
# 答え：
# 0
# 1
# 2
# 3
# 4

```

### スペース区切りで入力される単語、数値をリストにする
>問題：D052:ピラミッドの作り方
運動会の出し物で人間ピラミッドをやることになりました。ある段数のピラミッドを組むのに必要な人数を求めるプログラムをつくりましょう。ピラミッドでは以下のように上から i 段目には i 人が必要となります。N段のピラミッド必要な人数を出力してください。出力の最後に改行を 1 つ入れ、余計な文字、空行を含んではいけません。

```python
def sum_of_arithmetic_progression():
#    print("Hello Paiza")
    n = 0
    i = int(input("入力する整数は(0から6の間で):"))
    for i in range(1, i+1):
        #print(i)
        n += i
    print(n)
sum_of_arithmetic_progression()
```


### Checkio: 文章がある時頭は大文字、末に.を打つ
```Python
# my code
text = text[0].upper()+text[1:]
if text.endswith('.'):
    return text
else:
    text+='.'
    return text

# better solution
return text[0].upper() + text[1:] + ("." if text[-1] != "." else "")
```

### Checkio: returns the first word in a given text.
```Python
# my code
return text.lstrip(" .,").split()[0].split('.')[0].rstrip(" .,")
---------
# better solution
return text.replace(",", " ").replace(".", " ").split()[0]
```

## 02. print()
### format関数を使う(0は最初の参照、1は次の参照)  
```Python
print("{0}曜日は、{1}時間勉強する予定です。".format(dow,hour))`
````


## 03. リストを修正(追加、削除、更新)

```python
numbers = [100, 200, 300, 400, 500]
#後ろにつける
numbers.append(600)  #600つく
---------
# 要素追加
numbers.insert(3, 250)
---------
# 末尾の要素の削除
numbers.pop() #500消える
---------
# 2番目の要素の削除
numbers.pop(1) #200消える
---------
# 末尾の要素の変更
numbers[-1] = 1000
---------
# リストの内容を1つずつ表示
for i in numbers:
    print(i)
# 先頭を取り出して、末尾に移動しました。
last = numbers.pop(0)
numbers.append(last)
```

## 04. 集計

```Python
# used
# 利用状況
used = ['ボールペン', 'ノート', 'のり', 'のり', 'ノート']

# 集計用辞書
stationery_dict = {'ボールペン': 0,
                   'ノート': 0,
                   'のり': 0}

#各文房具の利用回数の計算
for stationery in used:
    # print(stationery)
    # ボールペン
    # ノート
    # のり
    # のり
    # ノート
    stationery_dict[stationery] += 1
    #for分で取得した名前を辞書の変数Inputにして、そこに１をたす
    # print(stationery_dict)
    # {'ボールペン': 1, 'ノート': 0, 'のり': 0}
    # {'ボールペン': 1, 'ノート': 1, 'のり': 0}
    # {'ボールペン': 1, 'ノート': 1, 'のり': 1}
    # {'ボールペン': 1, 'ノート': 1, 'のり': 2}
    # {'ボールペン': 1, 'ノート': 2, 'のり': 2}

# 結果の表示
print(stationery_dict)
#Ans
{'ボールペン': 1, 'ノート': 2, 'のり': 2}

#解説
#for文の1周目は、変数 stationery に「ボールペン」が代入されているので、 stationery_dict['ボールペン'] += 1 という計算が発生し、辞書 stationery_dict の値は {'ボールペン': 1, 'ノート': 0, 'のり': 0} となります。

#同様に2周目は、変数 stationery に「ノート」が代入されているので、 stationery_dict['ノート'] += 1 という計算が発生し、辞書 stationery_dict の値は {'ボールペン': 1, 'ノート': 1, 'のり': 0} となります。


---------
#会議室の予約数を集計する
book = {}

# ファイルinput/room.csvを開いて、集計
with open('input/room.csv', encoding='utf-8') as f:
    for row in f:
        columns = row.rstrip().split(',')
        #print(columns)
        #['会議室C', '高橋']
        #['会議室A', '加藤']
        #['会議室A', '木下']
        #['会議室A', '岡田']
        meeting_room = columns[0]

        if meeting_room in book:
            book[meeting_room] += 1
        else:
            book[meeting_room] = 1

# 表示
for room_name, count in book.items():
   print(room_name + ':' + str(count))


```



## 05. File操作（開く）

```python
#ファイルを開く
f = open('input/menu.csv', encoding='utf-8')
#開いた内容を読み込む
contents = f.read()
#表示する
print(contents)
#ファイルを閉じる
f.close()
---------
#with word を使った場合ファイルを開く
with open('input/menu.csv', encoding='utf-8') as f:
　　 #開いた内容を読み込む
    contents = f.read()
    #表示する
    print(contents)
---------
# 一番後ろの/nを無くしてファイル表示
with open('input/telephone.csv', encoding='utf-8') as f:
    for row in f:
        print(row.rstrip())
```
## 05. 文字列を分割
```Python
num_string = '100 200 300 400 500'
#スペースにはスペース’ ’を開けてとる
nums = num_string.split(' ')
for x in nums:
    print(x)

---------
一行を分割して表示
with open('input/menu.csv', encoding='utf-8') as f:
    for row in f:
        row_string = row.rstrip()
        columns = row_string.split(',')
        #print(columns)
        #['唐揚げ弁当', '400']
        #['とんかつ弁当', '550']
        #['ハンバーグ弁当', '500']
        #['上記のように続く']
        name = columns[0]
        price = columns[1]
        print(name + 'は' + price + '円')
---------
#電話当番一覧読込と分割
with open('input/telephone.csv', encoding='utf-8') as f:
    for row in f:
        row_f = row.rstrip().split(',')
        #print(row_f)
        day_of_week = row_f[0]
        in_charge = row_f[1]
        # 表示
        print(day_of_week + 'は' + in_charge + 'さんです。')
---------
#カラムの値を利用した計算とPrintのなかのsep""
print('<<2割引デー>>')
with open('input/menu.csv', encoding='utf-8') as f:
    for row in f:
        columns = row.rstrip().split(',')
        name = columns[0]
        price = int(columns[1])

        # 二割引きの計算
        discount = int(price * 0.8)
        print(name, 'は', discount, '円', sep='')
        #Ans
        # コロッケ弁当は320円
        # シャケ弁当は320円
        # 焼肉弁当は400円
        # 焼きそばは240円
        # カレーライスは280円
        # うな重は560円
        # ビビンバ丼は480

        #sepなしprint(name, 'は', discount, '円')
        # 唐揚げ弁当 は 320 円
        # とんかつ弁当 は 440 円
        # ハンバーグ弁当 は 400 円
        # のり弁当 は 280 円

---------
#ifで分岐する。
print('<<唐揚げ弁当半額デー>>')
with open('input/menu.csv', encoding='utf-8') as f:
    for row in f:
        columns = row.rstrip().split(',')
        name = columns[0]
        price = int(columns[1])

        # 唐揚げ弁当半額
        if name == "唐揚げ弁当":
            discount = int(price*0.5)
            print(name, ':', discount, '円(半額)', sep='')
        else:
            print(name, ':', price, '円', sep='')
---------
#ifで分岐、複数条件指定
print('<<丼100円引きデー>>')
with open('input/menu.csv', encoding='utf-8') as f:
    for row in f:
        columns = row.rstrip().split(',')
        name = columns[0]
        price = int(columns[1])
        # 100円引きの計算
        if name in ['うな重', 'ビビンバ丼']:
            discount = int(price - 100)
            print(name, ':', discount, '円', sep='')
        else:
            print(name, ':', price, '円', sep='')

```
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




## 0x. Numpy

```Python
import numpy as np

a = np.array([[1, 2],
             [3, 4]])

print(np.abs(a)) #絶対値を返します。
print(np.sqrt(a)) #平方根を返します。
print(np.square(a)) #2乗を返します。
print(np.exp(a)) #指数関数の値を返します。
print(np.log(a)) #自然対数の値を返します。
print(np.cos(a)) #三角関数の値を返します。他の三角関数についても演算が可能です。
print(np.cosh(a)) #双曲線関数の値を返します、他の双曲線関数についても演算が可能です。

print(a.T) #転置

```

## My Homework
### Q:公開認証鍵について素人にも分かるように簡潔に説明して
>ある死にかけの男が、拾った１億円もの大金を、自分の一番気に入っている女に渡そうと、円山町にあるDive Into Codeの金庫に隠し、女に引き取るように電話し、四桁の番号を設定したあと、「2210」と最後に女性に伝えて死にました。悪党がそれを見て聞いていました。
金庫の前で悪党と女が、その金庫の中身を持って行こうとしています。悪党は2210という番号は聞いていたものの、実際に2210を入れても開けらず諦めてしまいました。というのも男は実際は1192という番号で登録をしたからです。気に入った女性とその男性との間には、いつも秘密で使っている自分たちの共通の誕生日（10月18日）、気に入った車のナンバー1018があったのです。
```
上記の話には1018「共通鍵暗号」という概念があります。
まずここまでは、大昔から、男女の恋愛までよく用いられていたのです。悪党が見ていても、共通の鍵がないと開けられないというのはメリットなのでした。

素数と素因数分解という中学１年生が習う数学の概念を応用して、この発明がなされ、インターネットのサーバーなどのやりとりに用いられており、より安全に情報がやりとりができるようになっています。
```
