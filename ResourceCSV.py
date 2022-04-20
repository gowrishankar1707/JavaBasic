import os as sytem
import csv
import shutil
from tkinter import W
noOfResources=int(input("Enter the no of resources"))
noOfSchools=int(input("Enter the no of schools"))
schooName=str(input("Enter the schoolname"))
resourcId="resourceId_"

try:
    shutil.rmtree(sytem.path.join(sytem.getcwd(),"CSV"))
except FileNotFoundError as e:
    print(f"This directory not found{e}")



if not sytem.path.isdir(sytem.path.join(sytem.getcwd(),"CSV")):
    sytem.mkdir(sytem.path.join(sytem.getcwd(),"CSV"))


for rsc in range(0,(noOfResources)):
    for sch in range(0,(noOfSchools)):
        #print(f"{resourcId}__00{rsc},{schooName}_{sch}")
         with open(sytem.path.join(sytem.getcwd(),"CSV\\resources.csv"),'a',newline="") as createFile:
            csvWriter=csv.writer(createFile)
            data=[f"{resourcId}__00{rsc}",f"{schooName}_{sch}"]
            csvWriter.writerow(data)
        
    