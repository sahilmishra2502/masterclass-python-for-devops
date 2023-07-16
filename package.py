import os 
import shutil
print(os.getcwd())
total, used, free=  (shutil.disk_usage("/"))
print("total disk space is:",total// (2**30))
print("used disk space is:",used// (2**30))
print("free disk space is:",free// (2**30))