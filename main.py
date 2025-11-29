"""
main.py
示例脚本：从 Excel 文件读取数据并打印身份证号码列。

注意：此文件为简单示例，路径为示例路径，请根据实际情况修改文件路径。
"""

import pandas as pd


def read_excel(url, header=None):
    """读取 Excel 文件并返回 DataFrame。

    参数:
    - url (str): Excel 文件的路径或 URL。
    - header (int or None): 指定作为列名的行号（0-based）。如果为 None，则不使用标题行。

    返回:
    - pandas.DataFrame: 成功读取时返回 DataFrame。
    - None: 文件不存在或读取失败时返回 None（并打印错误信息）。
    """
    try:
        # 使用 pandas 读取 Excel 文件
        return pd.read_excel(url, header=header)
    except FileNotFoundError:
        # 文件路径不存在时给出提示并返回 None
        return print('路径不存在')


def main():
    """脚本主入口：读取指定 Excel 并打印 `公民身份号码` 列。

    当前示例使用硬编码的文件路径和 `header=1`，表示第二行作为列名。
    如果你的文件结构不同，请调整 `header` 参数或路径。
    """
    # 要读取的 Excel 文件路径（示例）。请根据实际情况修改。
    result = read_excel(
        r"D:\OneDrive - Panda Team\文档\Temp_data_01\RPA-学习\YD-KS"
        r"\20级计算机网络技术1班—新郑市大中专院校学生参加城乡基本医疗保险批量参保登记表.xlsx",
        header=1
    )

    # 检查是否成功读取，避免在 None 上索引导致异常
    if result is None:
        print('未能读取 Excel，程序退出')
        return

    # 打印名为 `公民身份号码` 的列
    print(result["公民身份号码"])


if __name__ == '__main__':
    main()