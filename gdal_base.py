from osgeo import gdal
import numpy as np

# 打开栅格数据文件
dataset = gdal.Open("path_to_your_raster_file.tif")

# 读取栅格数据为数组
band = dataset.GetRasterBand(1)  # 假设我们只读取第一个波段
array = band.ReadAsArray()

# 打印数组的形状、类型和内容
print("Shape of the array:", array.shape)
print("Type of the array:", type(array))
print("Array content:")
print(array)

# 获取栅格数据的宽度和高度
width = dataset.RasterXSize
height = dataset.RasterYSize

# 获取地理变换信息 (仿射变换参数)
geo_transform = dataset.GetGeoTransform()
print("Geo Transform:", geo_transform)

# 获取投影信息
projection = dataset.GetProjection()
print("Projection:", projection)

# 获取波段数量
num_bands = dataset.RasterCount
print("Number of Bands:", num_bands)

# 读取所有波段的数据
bands_data = []
for i in range(1, num_bands + 1):
    band = dataset.GetRasterBand(i)
    array = band.ReadAsArray()
    bands_data.append(array)

# 将所有波段的数据合并为一个多维数组
if num_bands > 1:
    all_bands_array = np.stack(bands_data, axis=-1)
else:
    all_bands_array = bands_data[0]

# 打印数组的形状、类型和内容
print("Shape of the array:", all_bands_array.shape)
print("Type of the array:", type(all_bands_array))
print("Array content:")
print(all_bands_array)

# 获取栅格数据的统计信息
for i in range(1, num_bands + 1):
    band = dataset.GetRasterBand(i)
    stats = band.GetStatistics(True, True)
    print(f"Band {i} Statistics: Min={stats[0]}, Max={stats[1]}, Mean={stats[2]}, StdDev={stats[3]}")

# 关闭数据集
dataset = None