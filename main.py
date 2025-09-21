#错误处理机制
try:
    x=1;
    y="123";
    print(x+y);
except TypeError:
    print("类型异常");