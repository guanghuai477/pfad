import pandas as pd
import matplotlib.pyplot as plt

# 加载 CSV 文件
file_path = r'E:\programming\latest_1min_temperature.csv'
df = pd.read_csv(file_path, skiprows=1, header=None)  # 跳过第一行标题

# 重命名列为时间、地点和温度
df.columns = ['时间/Time', '地点/Location', '温度/Temperature']

# 打印数据以确认
print("Renamed Columns:", df.columns)
print(df.head())

# 绘制基于地点的条形图，显示每个地点的温度
plt.figure(figsize=(12, 8))  # 调整图形尺寸为更宽的 12x8
plt.bar(df['地点/Location'], df['温度/Temperature'], color='skyblue')
plt.xlabel('Location')
plt.ylabel('Temperature (°C)')
plt.title('Temperature by Location')

# 调整标签的字体大小和旋转角度
plt.xticks(rotation=60, ha='right', fontsize=10)  # 旋转60度，向右对齐，字体大小10

# 显示图表
plt.tight_layout()
plt.show()
