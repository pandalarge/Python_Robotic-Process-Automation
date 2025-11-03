import pandas as pd
from datetime import datetime
import subprocess
import sys

# -------------------------- 自动安装依赖 --------------------------
def install_package(package):
    """自动安装指定Python包"""
    try:
        # 尝试导入，已安装则跳过
        __import__(package)
        print(f"✅ 已检测到 {package} 库，无需安装")
    except ImportError:
        # 未安装则自动安装
        print(f"⚠️  未检测到 {package} 库，正在自动安装...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", f"{package}==1.3.0"])
        print(f"✅ {package} 库安装完成")

# 安装保存Excel 97格式必需的xlwt库
install_package("xlwt")

# -------------------------- 核心逻辑 --------------------------
# 文件路径配置（输出为Excel 97格式.xls）
input_file_path = r'C:\Users\Admin\Desktop\凭证-样表.xlsx'  # 注意：你的用户名是Admin，已修正路径
output_file_path = r'C:\Users\Admin\Desktop\凭证-已排序.xls'

# 1. 读取原始Excel
df_full = pd.read_excel(input_file_path, dtype=object, keep_default_na=False)

# 2. 自动定位标题行和数据行
header_end_index = 0
for idx, row in df_full.iterrows():
    first_col_value = str(row.iloc[0]).strip()
    # 按凭证号特征（4位以上数字）找第一行数据
    if first_col_value.isdigit() and len(first_col_value) >= 4:
        header_end_index = idx
        break

# 拆分标题和数据
header_rows = df_full.iloc[:header_end_index].copy()
data_rows = df_full.iloc[header_end_index:].copy()

# 3. 按A列（凭证号）分组
vouchers = []
current_voucher = []
for _, row in data_rows.iterrows():
    first_col_value = str(row.iloc[0]).strip()
    if first_col_value.isdigit() and len(first_col_value) >= 4:
        if current_voucher:
            vouchers.append(current_voucher)
        current_voucher = [row]
    else:
        if current_voucher:
            current_voucher.append(row)
if current_voucher:
    vouchers.append(current_voucher)

# 4. 按D列（iloc[3]）日期排序
def safe_parse_date(date_value):
    clean_value = str(date_value).strip()
    for fmt in ['%Y-%m-%d', '%Y/%m/%d', '%Y年%m月%d日']:
        try:
            return datetime.strptime(clean_value, fmt)
        except:
            continue
    return datetime.max

vouchers.sort(key=lambda v: safe_parse_date(v[0].iloc[3]))

# 5. 合并并保存（Excel 97格式）
sorted_data = pd.concat([pd.DataFrame(v) for v in vouchers], ignore_index=True)
final_df = pd.concat([header_rows, sorted_data], ignore_index=True)

# 保存为Excel 97格式，指定Sheet名
try:
    with pd.ExcelWriter(output_file_path, engine='xlwt') as writer:
        final_df.to_excel(writer, sheet_name='凭证#单据头(FBillHead)', index=False)
    save_status = "成功（Excel 97 .xls格式）"
except Exception as e:
    # 备用方案：若xlwt安装失败，退化为.xlsx格式（避免完全无法使用）
    output_file_path = output_file_path.replace(".xls", ".xlsx")
    with pd.ExcelWriter(output_file_path, engine='openpyxl') as writer:
        final_df.to_excel(writer, sheet_name='凭证#单据头(FBillHead)', index=False)
    save_status = f"备用方案成功（.xlsx格式，原.xls格式失败：{str(e)[:50]}）"

# -------------------------- 结果提示 --------------------------
print("="*60)
print(f"✅ 凭证排序完成！保存状态：{save_status}")
print(f"📁 输出文件：{output_file_path}")
print(f"📄 Sheet名称：凭证#单据头(FBillHead)")
print("\n📊 排序后的凭证分组：")
for i, voucher in enumerate(vouchers, 1):
    vn = str(voucher[0].iloc[0]).strip()
    dt = str(voucher[0].iloc[3]).strip()
    print(f"   第{i}组：凭证号={vn} | D列日期={dt} | 行数={len(voucher)}")
print("="*60)