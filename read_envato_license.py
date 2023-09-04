############################# Created by AMIT GUPTA ######################################################

import impfunc                             ## import function file

## Get all files in directory
deffolder='C:\\Users\\trevi\\Downloads\\Envato Components'
#files = impfunc.list_files_in_directory('D:\\tempp\\Django_Admin_Panel')    ## define directory
print ("You have already defined folder to scan: ",deffolder)


## Getting only files from all folders
files = impfunc.list_files_in_directory(deffolder)    ## define directory
# files = impfunc.list_files_in_directory('D:\\Clientproject\\EnvatoElements\\webelements')    ## define directory



## get filterered files only txt extension files
filtered_files = [i for i in files if '.txt' in i]


## count files in folder
# c=impfunc.countfiles_in_directory('C:\\Users\\trevi\\Downloads\\Envato Components')
# print('count is :',c)

## list folder
ls_fol= impfunc.list_directory(deffolder)
# ls_fol= impfunc.list_directory('D:\\Clientproject\\EnvatoElements\\webelements')

# import pandas as pd
# print(l)


## Read all files one by one through this loop
dfs = []                                ### initialize new list
for file in filtered_files:
    # print(file)
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


## Save CSV using pandas method
import pandas as pd
df = pd.DataFrame(dfs) 
df.to_csv("exportthroughpanda.csv", index=False, mode='a', header=False)

## Save Excel using pandas method
import pandas as pd

df = pd.DataFrame(dfs)
filtered_files=pd.DataFrame(filtered_files)
ls_fol=pd.DataFrame(ls_fol)
# print(l)
# create a excel writer object
with pd.ExcelWriter(".\exportthroughpanda.xlsx") as writer:
    ls_fol.to_excel(writer, sheet_name='Folder_list', index=False)
    filtered_files.to_excel(writer, sheet_name='Files_list', index=False)
    df.to_excel(writer, sheet_name='License_list', index=False)
    # dfn.to_excel(writer, sheet_name='Folder_details', index=False)
    

# with pd.ExcelWriter(".\exportthroughpanda.xlsx",mode='a') as writer:
    # ls_fol.to_excel(writer, sheet_name='Folder_list',if_sheet_exists = 'overlay', index=False)
    # filtered_files.to_excel(writer, sheet_name='Files_list',if_sheet_exists = 'overlay', index=False)
    # df.to_excel(writer, sheet_name='License_list',if_sheet_exists = 'overlay', index=False)


###################################################################################################
#################################### V2 ###########################################################

############ Asking user to select folder for execution ##################
from tkinter import filedialog
from tkinter import *
root = Tk()
# root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
# print (root.filename)
folder_path = filedialog.askdirectory()
print ("You have chosen folder to scan: ",folder_path)

## Getting Folders and file names
dfm=impfunc.list_files_in_directory_new(folder_path)
import pandas as pd
# dft = pd.DataFrame([x.as_dict() for x in fl])
dfn = pd.DataFrame([vars(d) for d in dfm])
# print(dfn)

# ## Getting Folders and file names in dataframe
# dfm=impfunc.list_files_in_directory_new(deffolder)
# import pandas as pd
# # dft = pd.DataFrame([x.as_dict() for x in fl])
# dfn = pd.DataFrame([vars(d) for d in dfm])
# print(dfn)
print("-"*40)
print("No. of Folders:",len(pd.unique(dfn['location'])))
# extension = ['.zip']
# zipcount=dfn[dfn['name'].isin(extension)]
zipcount=dfn[dfn['name'].str.endswith('.zip')]
textcount=dfn[dfn['name'].str.endswith('.txt')]

print("No. of Zip files",len(zipcount))
print("No. of Text (License) files",len(textcount))
print("-"*40)

# p1=input("Do you want to extract data in excel sheet")
# print(p1)
# print("List of unique folders: ",dfn.location.unique())