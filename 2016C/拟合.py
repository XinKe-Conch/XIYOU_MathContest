import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
#T0 输入采样点开始的列数
T0 = 86
# n = 2 代表拟合的列数是20A  n=3 代表拟合的列数是30A .....以此类推
n = 2
# 定义目标函数 这里用指数型拟合参数曲线
def func1(x, a):
    return 3764-a* (x-9)**2
# 从Excel文件中读取数据
file_path = "CUMCM2016-C-Appendix-Chinese.xlsx"
df = pd.read_excel(file_path)  # 跳过第一行
# df = df.astype(float)

#第二列  20A的电压值
xary = np.array(df.iloc[T0-1:,n-1:n].values.flatten())
#第一列 放电时间
yary = np.array(df.iloc[T0-1:,0:1].values.flatten())
popt_1, pcov = curve_fit(func1, xary, yary)
plt.plot(xary, func1(xary, *popt_1),linestyle='--')
plt.scatter(xary,yary,marker='.',c='r',s=1)
plt.show()
print("拟合的曲线为：T=3764-{}*(x-9)^2".format((popt_1[0])))
