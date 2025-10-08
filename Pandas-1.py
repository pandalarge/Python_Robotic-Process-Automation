#引入pandas库 别名为 pd
import pandas as pd;
#读取excel需要基于openpyxl库，只要安装即可，无需引入
import openpyxl;
from pandas import DataFrame

#读取指定excel的指定sheet内数据
#excel=pd.read_excel('C:\\Users\\Panda\\Desktop\\文档-L\\数据表.xlsx',sheet_name='线下收款');

#------------------基础知识--------------------#

#创建Series(一维数组)
series_number=pd.Series(['190','235','999']);
#转换数据类型为数值类型
series_number=pd.to_numeric(series_number);
#做运算
series_number=series_number/2;
series_name=pd.Series(['香蕉','玉米','鸡蛋']);
#合并为DataFrame
df=pd.DataFrame({'名字':series_name,'数量':series_number});

DataFrame.to_excel(df,'C:\\Users\\Panda\\Desktop\\文档-L\\数据表.xlsx',sheet_name='应收单',mode='a',engine='xlsxwriter');

#创建DataFrame(二维数组)
data={'name':['马思莹','李春旺'],'age':['23','23']}
df=pd.DataFrame(data);


