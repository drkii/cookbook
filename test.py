n = 0
i = int(input("入力する整数は(0から6の間で):"))
for i in range(1, i+1):
    #print(i)
    n += i
print(n)


# coding: utf-8

# In[1]:


import numpy as np
from sklearn.datasets import load_boston
boston = load_boston()
import pandas as pd
X=pd.DataFrame(boston.data[:100,:], columns=boston.feature_names)
y=boston.target[:100]


# In[2]:


x=X['LSTAT'].values


# In[3]:


import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
plt.scatter(x,y)


# In[4]:


from sklearn.linear_model import LinearRegression
lin_1d = LinearRegression()


# In[18]:


#xを縦ベクトルに変換
#x[:, np.newaxis]も同様

lin_1d.fit(x[:,None],y)


# In[6]:


lin_1d.predict(2)
lin_1d.predict(10)


# In[7]:


#まずプロット用のデータを用意します。
n = np.linspace(np.min(x),np.max(x), 1000)
y_1d_fit=lin_1d.predict(n[:,np.newaxis])

plt.title("Boston House Price")
plt.scatter(x,y,label='data')
plt.plot(n,y_1d_fit,'r',label='1d_lin')
plt.ylim(10,40)#グラフを見やすくするためにｙ軸のプロット範囲を絞っているだけです。
plt.xlabel("LSTAT")
plt.ylabel("price")
plt.legend()
plt.plot()


# In[8]:


lin_1d.predict(25)


# In[10]:


from sklearn.preprocessing import PolynomialFeatures
degree_2=PolynomialFeatures(degree=2)


# In[12]:


x_2=degree_2.fit_transform(x[:,None])
x_2


# In[14]:


lin_2d = LinearRegression()
lin_2d.fit(x_2,y)


# ## ここから課題①

# ### まずは3次関数の回帰

# In[27]:


# 3次までの変数を作成するインスタンス
degree_3 = PolynomialFeatures(degree = 3)


# In[28]:


# 変数を作成
x_3=degree_3.fit_transform(x[:,None])
x_3


# In[30]:


lin_3d = LinearRegression()
#3次の項を追加
lin_3d.fit(x_3,y)


# ### 同様に4次関数の回帰

# In[32]:


# 4次までの変数を作成するインスタンス
degree_4 = PolynomialFeatures(degree = 4)


# In[33]:


# 変数を作成
x_4=degree_4.fit_transform(x[:,None])
x_4


# In[34]:


lin_4d = LinearRegression()
#4次の項を追加
lin_4d.fit(x_4,y)


# ### 1〜4次関数をプロット

# In[35]:


#プロット用のデータを用意
n = np.linspace(np.min(x),np.max(x), 1000)

#1〜4次関数の予測値
y_4d_fit=lin_4d.predict(degree_4.fit_transform(n[:,np.newaxis]))
y_3d_fit=lin_3d.predict(degree_3.fit_transform(n[:,np.newaxis]))
y_2d_fit=lin_2d.predict(degree_2.fit_transform(n[:,np.newaxis]))
y_1d_fit=lin_1d.predict(n[:,np.newaxis])

plt.title("Boston House Price")
plt.scatter(x,y,label='data')

#1〜4次関数をプロット
plt.plot(n,y_4d_fit,'c',label='4d_lin')
plt.plot(n,y_3d_fit,'b',label='3d_lin')
plt.plot(n,y_2d_fit,'g',label='2d_lin')
plt.plot(n,y_1d_fit,'r',label='1d_lin')

plt.ylim(10,40)　#グラフを見やすくするためにｙ軸のプロット範囲を絞る
plt.xlabel("LSTAT")
plt.ylabel("price")
plt.legend()
plt.plot()


# In[39]:


#平均2乗誤差 (MSE)を計算する
from sklearn.metrics import mean_squared_error
#1次関数の2乗和誤差
error_d1 = mean_squared_error(y,lin_1d.predict(x[:,None]))
error_d1


# In[40]:


#２次関数の2乗和誤差
error_d2 = mean_squared_error(y,lin_2d.predict(x_2))
error_d2


# In[41]:


#3次関数の2乗和誤差
error_d3 = mean_squared_error(y,lin_3d.predict(x_3))
error_d3


# In[43]:


#4次関数の2乗和誤差
error_d4 = mean_squared_error(y,lin_4d.predict(x_4))
error_d4


# ### したがって、error_d1〜error_d4を比較すると、4次関数の2乗和誤差が一番小さい
