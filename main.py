import pandas as pd

def read_excel(url,header=None):
    try:
        return pd.read_excel(url,header=header)
    except FileNotFoundError:
        return print('路径不存在')

def main():
    result=read_excel(
        r"D:\OneDrive - Panda Team\文档\Temp_data_01\RPA-学习\YD-KS"
        r"\20级计算机网络技术1班—新郑市大中专院校学生参加城乡基本医疗保险批量参保登记表.xlsx",
        header=1
    )
    print(result["公民身份号码"])

if __name__ == '__main__':
    main()