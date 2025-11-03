#引入pandas库 别名为 pd
import sys

import pandas as pd;
#读取excel需要基于openpyxl库，只要安装即可，无需引入
import openpyxl;

#读取CSV文件-Python的斜杠路径可以用r或者双斜杠来处理
data_csv=pd.read_csv(r'C:\Users\Panda\Desktop\YD-KS\titanic.csv')
print(data_csv)





