#%%
import requests
import time
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as md
import numpy as np
import datetime as dt
#%%
pd.set_option('expand_frame_repr', False)
base_url = 'https://api.binance.com'
kline = '/api/v1/klines'
# kline_url = base_url + kline + '?' + 'symbol=BTCUSDT&interval=1h&limit=1000'
# resp = requests.get(kline_url)
# df = pd.DataFrame(resp.json())
# #%%
# print(df)
# # %%
# df.to_excel('/home/kai/文件/btcdata/'+'test'+'.xlsx', index = False)
#%%
# low_bound =1503158400000 #2017/08/20 00:00:00
# limit = 1000
# end_time = int(time.time() // 60 * 60 * 1000)
# start_time = int(end_time - limit *60 *1000)
# df = pd.DataFrame()
# while True:
#     df = pd.DataFrame()
#     if (start_time < low_bound):
#         break    
#     url = base_url + kline + '?' + 'symbol=BTCUSDT&interval=1m&limit=' +str(limit) + '&startTime=' + str(start_time) 
#     resp = requests.get(url)
#     data = resp.json()
#     df = pd.DataFrame(data, columns={'open_time': 0, 'open' : 1, 'high' : 2, 'low' : 3, 'close' : 4, 'volume' : 5, 'close_time' : 6, 'quote_volume' : 7, 'trades' : 8, 'taker_base_volue' : 9, 'taker_quote_volume' : 10, 'ignore' : 11} )
#     df.insert (1, "time", pd.to_datetime(df['open_time'], unit='ms'))
#     #df['open_time'] = pd.to_datetime(df['open_time'], unit='ms')
#     df.set_index('open_time', inplace=True)
#     df.to_excel('/home/kai/文件/btcdata_1m/'+str(end_time)+'.xlsx',)
#     print(df)
#     end_time = start_time
#     start_time =  int(start_time - limit *60 *1000)
#%%
low_bound =1503158400000 #2017/08/20 00:00:00
limit = 1000
end_time = int(time.time() // 60 * 60 * 1000)
start_time = int(end_time - limit *60 *1000*60*24)
df = pd.DataFrame()
while True:
    df = pd.DataFrame()
    if (start_time < low_bound):
        break    
    url = base_url + kline + '?' + 'symbol=BTCUSDT&interval=1d&limit=' +str(limit) + '&startTime=' + str(start_time) 
    resp = requests.get(url)
    data = resp.json()
    df = pd.DataFrame(data, columns={'open_time': 0, 'open' : 1, 'high' : 2, 'low' : 3, 'close' : 4, 'volume' : 5, 'close_time' : 6, 'quote_volume' : 7, 'trades' : 8, 'taker_base_volue' : 9, 'taker_quote_volume' : 10, 'ignore' : 11} )
    df.insert (1, "time", pd.to_datetime(df['open_time'], unit='ms'))
    #df['open_time'] = pd.to_datetime(df['open_time'], unit='ms')
    df.set_index('open_time', inplace=True)
    df.to_excel('/home/kai/文件/btcdata_1d/'+str(end_time)+'.xlsx',)
    print(df)
    end_time = start_time
    start_time =  int(start_time - limit *60 *1000*60*24)

# %%
df1 = pd.read_excel('/home/kai/文件/btcdata_1m/'+'1503275820000'+'.xlsx')

# %%
x = [0.00001,0.001,0.01,0.1,0.5,1,5]
y = [0.945,0.885,0.893,0.9,0.996,1.25,1.19]
plt.xlim(0.00001,5)
plt.ylim(0.8,1.4)
plt.plot(x, y, marker='o', linestyle='--', color='r', 
label='Square') 
plt.xlabel('x')
plt.ylabel('y') 
plt.title('compare')
plt.legend() 
plt.show()
# %%
x = [0.00001,0.001,0.01,0.1,0.5,1,5]
# create an index for each tick position
xi = range(len(x))
y = [0.945,0.885,0.893,0.9,0.996,1.25,1.19]
plt.ylim(0.8,1.4)
# plot the index for the x-values
plt.plot(xi, y, marker='o', linestyle='--', color='r', label='Square') 
plt.xlabel('x')
plt.ylabel('y') 
plt.xticks(xi, x)
plt.title('compare')
plt.legend() 
plt.show()
# %%
plt.figure(figsize=(20,5))
plt.plot(df1['time'], df1['open'])
# %%
plt.figure(figsize=(20,5))
ax=plt.gca()
xfmt = md.DateFormatter('%Y-%m-%d %H:%M:%S')
ax.xaxis.set_major_formatter(xfmt)
#plt.xticks(rotation=90)
plt.plot(df1["time"], df1['open'])

# %%
df = pd.DataFrame()
start = 1503275820000
end = 1598495820000 + 1
for i in range(start,end,60*1000*1000):
    df_temp = pd.read_excel('/home/kai/文件/btcdata_1m/'+str(i)+'.xlsx')
    df = pd.concat([df,df_temp])
    print(i)
# %%
df.to_excel('/home/kai/文件/btcdata_1m/'+'total_data_1min'+'.xlsx')
# %%
df1 = df(len(df)/2)
# %%
dfs = np.split(df, [int(1588000/2)], axis=0)
# %%
dfs[0].to_excel('/home/kai/文件/btcdata_1m/'+'total_data_1min_1'+'.xlsx')
# %%
dfs[1].to_excel('/home/kai/文件/btcdata_1m/'+'total_data_1min_2'+'.xlsx')
# %%
df = pd.read_excel('/home/kai/文件/btcdata_1m/'+'total_data_1min_1'+'.xlsx')
# %%
df1 = pd.read_excel('/home/kai/文件/btcdata_1m/'+'total_data_1min_2'+'.xlsx')
# %%
df = pd.concat([df,df1])
# %%
df=df.drop(['Unnamed: 0'],axis=1)
#%%
df.info()
# %%
df.describe()
# %%
df.columns
# %%
corr = df.corr()
# %%
import seaborn as sn
f, ax = plt.subplots(figsize=(10, 8))
sn.heatmap(corr, mask=np.zeros_like(corr, dtype=np.bool), cmap=sn.diverging_palette(220, 10, as_cmap=True),square=True, ax=ax)
f
#%%
plt.figure(figsize=(20,10))
ax=plt.gca()
xfmt = md.DateFormatter('%Y-%m-%d %H:%M:%S')
ax.xaxis.set_major_formatter(xfmt)
plt.xticks(rotation=45)
plt.plot(df["time"], df['open'])


# %%
