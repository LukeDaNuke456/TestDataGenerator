Vehicle Data Generator 

Instructions (Windows based):

    1. Download this repo to your machine inside of a folder of your choosing.
    2. Start up powershell / cmd and navigate to the folder and 'cd' into it. 
    3. Create virtual enviornment and activate it.
    4. Use pip to install these packages: 

        a. 
        b. 
        c.


Descritpion:
This program will create Vehcile data. Each vehicle will have these attributes: 

    1. Vehicle ID
    2. Vehicle Year
    3. Vehicle Make
    4. Vehicle Model
    5. Vehicle Mileage
    6. Vehicle Price.

There is an algorithm within the createtestdata.py that will assign attributes based on criteria. 

  1. Vehicle model is dependent on Vehicle make.
  2. Vehicle mileage is dependent on year **assuming that the vehicle has been driven over the course of a few years**.
  3. Vehicle price is determined based on every attribute other than ID.

**RESEARCH AND DEVELOPMENT OF THIS ALGORITHM IS STILL ONGOING**
**UPDATES TO README.txt WILL BE COMING FOR BETTER INSTRUCTIONS**

To use this optimally, I reccommend using the Jupyter Notebook to run the multiple python scripts. Just 
open the notebook, and run the script entirely. There will be a excel workbook created by doing this. 
**NOTE: If you run the script again, the old excel file will be deleted and replaced with the new data you create.
