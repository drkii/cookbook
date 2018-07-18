
# Python Cookbook

## 01. 入力を扱う
### スペース区切りで入力される文字列、数値をリストにする
```python
#文字列
words = [i for i in input().split()]
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

# better solution
return text.replace(",", " ").replace(".", " ").split()[0]
```

## 02. print()
### format関数を使う(0は最初の参照、1は次の参照)  
`print("{0}曜日は、{1}時間勉強する予定です。".format(dow,hour))`


## 03. リストを修正(追加、削除、更新)

```python
numbers = [100, 200, 300, 400, 500]
#後ろにつける
numbers.append(600)  #600つく
# 要素追加
numbers.insert(3, 250)
# 末尾の要素の削除
numbers.pop() #500消える
# 2番目の要素の削除
numbers.pop(1) #200消える
# 末尾の要素の変更
numbers[-1] = 1000
# リストの内容を1つずつ表示
for i in numbers:
    print(i)
# 先頭を取り出して、末尾に移動しました。
last = numbers.pop(0)
numbers.append(last)
```

## 04. File操作（開く）

```python
#ファイルを開く
f = open('input/menu.csv', encoding='utf-8')
#開いた内容を読み込む
contents = f.read()
#表示する
print(contents)
#ファイルを閉じる
f.close()

#with word を使った場合ファイルを開く
with open('input/menu.csv', encoding='utf-8') as f:
　　 #開いた内容を読み込む
    contents = f.read()
    #表示する
    print(contents)

```

## 05. Numpy

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
