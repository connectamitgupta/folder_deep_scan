############################# Created by AMIT GUPTA ######################################################

import impfunc                             ## import function file

## Get all files in directory
#files = impfunc.list_files_in_directory('D:\\tempp\\Django_Admin_Panel')    ## define directory

files = impfunc.list_files_in_directory('C:\\Users\\trevi\\Downloads\\Envato Components')    ## define directory


## get filterered files only txt extension files
filtered_files = [i for i in files if '.txt' in i]

## Read all files one by one through this loop
dfs = []                                ### initialize new list
for file in filtered_files:
    print(file)
#   df = pd.read_csv(file,sep='\t')
    df=impfunc.licensereadbulk(file)       ### Use custom function to extract data from files
    # print(df)
    dfs.append(df)                      ### append list item 
# print(type(dfs))


## Export in CSV format
## Preliminary step for define header row
import csv
# ky = dfs[0]                                 ### Get list's first index
# print(ky)
keys=dfs[0].keys()                            ### Get list's first keys data for header
# print(keys)

## Save header and row wise information in CSV
with open('exportthroughnative.csv', 'a', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(dfs)

## Save using pandas method
import pandas as pd
df = pd.DataFrame(dfs) 
df.to_csv("exportthroughpanda.csv", index=False, mode='a', header=False)