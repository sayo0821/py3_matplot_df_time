# -*- coding: utf8 -*-

# --------    ここから 初期作業    --------
# 実行パスを追加(プログラム実行の一番最初でやるのが無難)。
# Emddable Pythonやpyinstaller等でexe化して実行する場合などの対策用。
# モジュール検索パスは標準ライブラリのsysモジュールのsys.pathに格納されている。
# プログラム終了後は、sys.pathはOSシステム等に残らない(確認済)。
# カレントディレクトリ変更(os.chdir)だけではEmddable Pythonではうまくいかないこともあったため両方記載。
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
# --------    ここまで 初期作業    --------


# --------    ここから 使用ライブラリ等の記載    --------
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
# --------    ここまで 使用ライブラリ等の記載    --------


# csvをdfに変換
file_path = 'data001.csv'
df = pd.read_csv(file_path)

# dfのグラフにする範囲を指定、ここでは2列目から8列目までを対象とした記載
df = df.iloc[1:9,]

# dfで文字列の時刻データをdatetime型に変換
# matplotlibのX軸を時系列にするときmdates.DateFormatterで変換するため
df['time'] = pd.to_datetime(df['time'])

# 日本語表示用の設定
plt.rcParams['font.family'] = "MS Gothic"
plt.rcParams['font.size'] = 8

# 無地のキャンバスを作成する
fig, ax = plt.subplots(1,1, dpi=100,figsize=(8, 4))
fig.autofmt_xdate()    # X軸下部のラベルが見えなくなる対応

ax.plot(df["time"], df["temp"])

# matplotlibのX軸を時系列にする
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))

# X軸の区切りを秒単位として10秒間隔とした場合。
secLoc = mdates.SecondLocator(bysecond=None, interval=10, tz=None)
ax.xaxis.set_major_locator(secLoc)

# グラフの表示
plt.show()



'''
【参考】
Matplotlib 時系列データの軸設定｜自由に時間軸を設定！
https://www.yutaka-note.com/entry/matplotlib_time_axis

'''
