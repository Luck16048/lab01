import datetime
import sys
from sys import version_info

name = "Tali"

current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
version_info = sys.version

print("Name: " + name)
print("Current date: " + current_date)
print("Version Python: " + version_info)