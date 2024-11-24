from osgeo import gdal
import numpy as np
import matplotlib.pyplot as plt

# 打开栅格数据文件
dataset = gdal.Open("path_to_your_raster_file.tif")

# 读取栅格数据为数组
band = dataset.GetRasterBand(1)  # 假设我们只读取第一个波段
array = band.ReadAsArray()

# 显示图像
plt.figure(figsize=(10, 10))
plt.imshow(array, cmap='gray')  # 使用灰度图显示单波段图像
plt.title("Raster Image")
plt.colorbar(label='Intensity')
plt.show()

# 关闭数据集
dataset = None



from osgeo import gdal
import numpy as np
import matplotlib.pyplot as plt

# 打开栅格数据文件
dataset = gdal.Open("path_to_your_raster_file.tif")

# 读取所有波段的数据
bands_data = []
for i in range(1, dataset.RasterCount + 1):
    band = dataset.GetRasterBand(i)
    array = band.ReadAsArray()
    bands_data.append(array)

# 将所有波段的数据合并为一个多维数组
if dataset.RasterCount > 1:
    all_bands_array = np.stack(bands_data, axis=-1)
else:
    all_bands_array = bands_data[0]

# 显示图像
plt.figure(figsize=(10, 10))
if dataset.RasterCount == 1:
    plt.imshow(all_bands_array, cmap='gray')  # 使用灰度图显示单波段图像
else:
    plt.imshow(all_bands_array)  # 使用默认颜色映射显示多波段图像
plt.title("Raster Image")
plt.colorbar(label='Intensity')
plt.show()

# 关闭数据集
dataset = None



from osgeo import gdal
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

# 打开栅格数据文件
dataset = gdal.Open("path_to_your_raster_file.tif")

# 读取栅格数据为数组
band = dataset.GetRasterBand(1)  # 假设我们只读取第一个波段
array = band.ReadAsArray()

# 获取地理变换信息
geo_transform = dataset.GetGeoTransform()

# 获取投影信息
projection = dataset.GetProjection()

# 创建一个cartopy投影对象
crs = ccrs.epsg(int(projection.split(':')[-1]))

# 显示图像
plt.figure(figsize=(10, 10))
ax = plt.axes(projection=crs)
ax.imshow(array, origin='upper', extent=(geo_transform[0], geo_transform[0] + dataset.RasterXSize * geo_transform[1],
                                         geo_transform[3] + dataset.RasterYSize * geo_transform[5], geo_transform[3]),
          transform=crs, cmap='gray')
ax.gridlines(draw_labels=True)
plt.title("Raster Image with Geographic Reference")
plt.show()

# 关闭数据集
dataset = None