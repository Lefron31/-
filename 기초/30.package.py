#모듈을 모아둔 파일

# from travel.thailand import *
# trip_to = ThailandPackage()
# trip_to.detail()


from travel import *
trip_to = vietnam.VietnamPackage()
trip_to.detail()
trip_to = thailand.ThailandPackage()
trip_to.detail()


import inspect
print(inspect.getfile(thailand))