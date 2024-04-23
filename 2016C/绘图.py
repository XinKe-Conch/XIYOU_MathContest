import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
# 从Excel文件中读取数据
file_path = "CUMCM2016-C-Appendix-Chinese.xlsx"
df = pd.read_excel(file_path ,sheet_name="附件1    ")

# 将数据转换为浮点数
df = df.astype(float)
fig, ax = plt.subplots()

# iterate over each column
for column in df.columns[1:]:
    print(df[column])
    ax.plot(df[column], df.index, label=column)


ax.legend()
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.ylabel('剩余放电时间（分钟）')
plt.xlabel('电压（伏特）')
plt.title('电压随剩余时间变化图（不同电流）')
plt.show()
