import pandas as pd;
#创建Series一维列表
ages=pd.Series([15,28,69,12,43],name='ages');
print(ages.max());

#创建DataFrame二维列表
tables=pd.DataFrame({
    'No':[1,2,3,4,5,6],
    'Name':['Tom','joh','panda','kt','leite','3dm']
})
print(tables['No'].max());
#获取列表的 basic statistic of numerical data
print(tables.describe());
