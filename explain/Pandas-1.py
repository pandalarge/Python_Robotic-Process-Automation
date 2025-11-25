#引入pandas库 别名为 pd
import sys

import pandas as pd;
#读取excel需要基于openpyxl库，只要安装即可，无需引入
import openpyxl;

#读取CSV文件-Python的斜杠路径可以用r或者双斜杠来处理
data_csv=pd.read_csv(r'D:\OneDrive - Panda Team\文档\Temp_data_01\RPA-学习\YD-KS\air_quality_no2.csv',index_col=0,parse_dates=True);
data_csv["翻倍"]=data_csv['station_london']*2+data_csv['station_london'];
print(data_csv.groupby("station_london").mean());





