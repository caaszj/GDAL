from osgeo import gdal

a = gdal.Open("")
a = a.ReadAsArray()
print(a.shape)
print(type(a))
print(a)