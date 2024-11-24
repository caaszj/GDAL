from osgeo import gdal

a = gdal.Open("/content/drive/MyDrive/000005_GF.tif")
a = a.ReadAsArray()
print(a.shape)
print(type(a))
print(a)

