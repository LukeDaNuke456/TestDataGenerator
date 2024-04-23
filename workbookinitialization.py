import os
from openpyxl import Workbook

wb = Workbook()

filename = "vehicle_data.xlsx"

if os.path.exists(filename):
    os.remove(filename)
    print(f"Old Workbook '{filename}' deleted. Creating a new one..")
    wb.save("vehicle_data.xlsx")
    exec(open( "createtestdata.py").read())
else: 
    print(f"Workbook '{filename}' does not exist. Creating a new one.. ")
    wb.save("vehicle_data.xlsx")
    exec(open( "createtestdata.py").read())
    