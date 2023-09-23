import impfunc                             ## import function file
import pandas as pd
from tkinter import filedialog
from tkinter import *
import json                 ## Import json helper module
from colorama import Fore,Back, Style

############################# Created by AMIT GUPTA ######################################################
################# Version 1 program
def menuchosen_v1(output_type):


    ## Get all files in directory
    # deffolder='D:\Clientproject\EnvatoElements\Envbackup'
    deffolder=r'D:\Clientproject\EnvatoElements\test'
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
    with open('.\export_files\exportthroughnative.csv', 'a', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(dfs)


    ## Save CSV using pandas method
    df = pd.DataFrame(dfs) 
    df.to_csv(".\export_files\exportthroughpanda.csv", index=False, mode='a', header=False)

    #### Save Excel using pandas method
    
    ### converting list to pandas dataframes
    df = pd.DataFrame(dfs)
    filtered_files=pd.DataFrame(filtered_files)
    ls_fol=pd.DataFrame(ls_fol)
    # print(l)

    if output_type==1:
    # create a excel writer object
        with pd.ExcelWriter(".\export_files\exportthroughpanda.xlsx") as writer:
            ls_fol.to_excel(writer, sheet_name='Folder_list', index=False)
            filtered_files.to_excel(writer, sheet_name='Files_list', index=False)
            df.to_excel(writer, sheet_name='License_list', index=False)
            # dfn.to_excel(writer, sheet_name='Folder_details', index=False)
        msg=Fore.GREEN+"Folder scanned and File created successfully"
    elif output_type==2:
        # msg="check json now"
        ## Created new dictionary and assigned existing dataframe as json child object by converting datarame to json
        # concatdata={"Folder_list":ls_fol,"Files_list":filtered_files}
        # ls_fol.to_json()
        # print(df)
        concatdata={"Folder_list":ls_fol.to_json(),"Files_list":filtered_files.to_json(),"License_list":df.to_json()}
        # df.values.toli3st()
        # concatdata=pd.DataFrame(concatdata, index=0)
        # print(concatdata)
        # concatdata.to_json(r'.\export_files\exportthroughpanda.json',)
        ## writing down new file
        with open(".\export_files\exportthroughpanda.json", "w") as outfile:
            json.dump(concatdata, outfile)
        msg=Fore.GREEN+'Folder scanned and XLSX Files created successfully'
    else:
        msg=Fore.RED+"No valid type was chosen."


    return msg
###################################################################################################
#################################### V2 ###########################################################

def menuchosen_v2(output_type):

    ############ Asking user to select folder for execution ##################
    # from tkinter import filedialog
    # from tkinter import *
    root = Tk()
    # root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    # print (root.filename)
    print (Back.YELLOW+Fore.RED+"########### Choose appropriate folder to scan now....... ")
    folder_path = filedialog.askdirectory(title="select folder to start with")
    root. destroy()
    print(Style.RESET_ALL)

    print ("...You have chosen folder to scan: ",folder_path)

    ### Getting Folders and file names throough function and get multiple objects
    dfc, dfm=impfunc.list_files_in_directory_new(folder_path)
    # dft = pd.DataFrame([x.as_dict() for x in fl])
    
    ### all files information and seperate object columns and save as dataframe
    # dfm = pd.DataFrame([vars(d) for d in dfm])
        # print(dfm)

    ## Getting only files from all folders
    files = impfunc.list_files_in_directory(folder_path)    ## define directory



    ## get filterered files only txt extension files
    filtered_files = [i for i in files if '.txt' in i]
    # print(filtered_files)

    ## Read all files one by one through this loop
    dfs = []                                ### initialize new list
    for file in filtered_files:
        # print(file)
    #   df = pd.read_csv(file,sep='\t')
        a=impfunc.licensereadbulk(file)       ### Use custom function to extract data from files
        # print(df)
        dfs.append(a)                      ### append list item 
    # print(type(dfs))


    try:
        #### Temporary block
        print("-"*40)
        print("No. of Folders:",len(pd.unique(dfm['folder_location'])))
        # extension = ['.zip']
        # zipcount=dfn[dfn['name'].isin(extension)]
        zipcount=dfm[dfm['file_name'].str.endswith('.zip')]
        textcount=dfm[dfm['file_name'].str.endswith('.txt')]

        print("No. of Zip files",len(zipcount))
        print("No. of Text (License) files",len(textcount))
        print("-"*40)
        ### Temporary block ends here
    except:
        pass

    ### Statstics information
    dfc_len=len(dfc)
    dfm_len=len(dfm)
    dfinfo_len=len(dfs)
    
    stat=Fore.YELLOW+f"\n No. of folders: {dfc_len}\n No. of files: {dfm_len}\n No. of license files: {dfinfo_len} "
    

#### Converting list of objects  to pandas dataframe
    ### folder information seperate object columns and save as dataframe
    dfc=pd.DataFrame([vars(d) for d in dfc])
    # print(dfc)

    ### all files information and seperate object columns and save as dataframe
    dfm = pd.DataFrame([vars(d) for d in dfm])
        # print(dfm)

    ### deep scanned file info all info 
    dfinfo=pd.DataFrame(dfs)

    if output_type==1:
        with pd.ExcelWriter(".\export_files\india.xlsx") as writer:
            dfc.to_excel(writer, sheet_name='Folder_information', index=False, header=True)
            dfm.to_excel(writer, sheet_name='Files_information', index=False, header=True)
            dfinfo.to_excel(writer, sheet_name='DeepFileinformation', index=False, header=True)

        # dfc.to_json('file1.json', orient = 'split', compression = 'infer')
        msg=Fore.GREEN+'Folder scanned and XLSX Files created successfully'+stat
    elif output_type==2:
        # msg=Fore.GREEN+"check json now"
        ## Created new dictionary and assigned existing dataframe as json child object by converting datarame to json
        # concatdata={"Folder_list":ls_fol,"Files_list":filtered_files}
        # print(dfc)
        concatdata={"Folder_list":dfc.to_json(),"Files_list":dfm.to_json(),"License_list":dfinfo.to_json()}
        with open(".\export_files\deepanalysis.json", "w") as outfile:
            json.dump(concatdata, outfile)
        msg=Fore.GREEN+'Folder(s) scanned and json File created successfully'+stat
    else:
        msg=Fore.RED+"No valid type was chosen."


    return msg


#################################################################################################
##################### V3 ########################################################################

def menuchosen_v3(output_type):

    ############ Asking user to select folder for execution ##################
    # from tkinter import filedialog
    # from tkinter import *
    root = Tk()
    # root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    # print (root.filename)
    print (Back.YELLOW+Fore.RED+"########### Choose appropriate folder to scan now....... ")
    source_folder_path = filedialog.askdirectory(title="select folder to start with")
    root. destroy()
    print(Style.RESET_ALL)
    print ("...You have chosen folder to scan: ",source_folder_path)


    # print (Back.YELLOW+Fore.RED+"########### Select Git Folder....... ")
    # Git_folder_path = filedialog.askdirectory(title="select Git to start with")
    # root. destroy()
    # print(Style.RESET_ALL)




    ### Getting Folders and file names throough function and get multiple objects
    dfc, dfm=impfunc.list_files_in_directory_v3(source_folder_path)
    # dft = pd.DataFrame([x.as_dict() for x in fl])
    
    ### all files information and seperate object columns and save as dataframe
    # dfm = pd.DataFrame([vars(d) for d in dfm])
        # print(dfc)
        # print(dfm)

    ## Getting only files from all folders
    files = impfunc.list_files_in_directory(source_folder_path)    ## define directory



    ## get filterered files only txt extension files
    filtered_files = [i for i in files if '.txt' in i]
    # print(filtered_files)

    ## Read all files one by one through this loop
    dfs = []                                ### initialize new list
    for file in filtered_files:
        # print(file)
    #   df = pd.read_csv(file,sep='\t')
        a=impfunc.licensereadbulk(file)       ### Use custom function to extract data from files
        # print(df)
        dfs.append(a)                      ### append list item 
    # print(type(dfs))


    try:
        #### Temporary block
        print("-"*40)
        print("No. of Folders:",len(pd.unique(dfm['folder_location'])))
        # extension = ['.zip']
        # zipcount=dfn[dfn['name'].isin(extension)]
        zipcount=dfm[dfm['file_name'].str.endswith('.zip')]
        textcount=dfm[dfm['file_name'].str.endswith('.txt')]

        print("No. of Zip files",len(zipcount))
        print("No. of Text (License) files",len(textcount))
        print("-"*40)
        ### Temporary block ends here
    except:
        pass

    ### Statstics information
    dfc_len=len(dfc)
    dfm_len=len(dfm)
    dfinfo_len=len(dfs)
    
    stat=Fore.YELLOW+f"\n No. of folders: {dfc_len}\n No. of files: {dfm_len}\n No. of license files: {dfinfo_len} "
    

#### Converting list of objects  to pandas dataframe
    ### folder information seperate object columns and save as dataframe
    dfc=pd.DataFrame([vars(d) for d in dfc])
    # print(dfc)

    ### all files information and seperate object columns and save as dataframe
    dfm = pd.DataFrame([vars(d) for d in dfm])
        # print(dfm)

    ### deep scanned file info all info 
    dfinfo=pd.DataFrame(dfs)

    if output_type==1:
        with pd.ExcelWriter(".\export_files\india.xlsx") as writer:
            dfc.to_excel(writer, sheet_name='Folder_information', index=False, header=True)
            dfm.to_excel(writer, sheet_name='Files_information', index=False, header=True)
            dfinfo.to_excel(writer, sheet_name='DeepFileinformation', index=False, header=True)

        # dfc.to_json('file1.json', orient = 'split', compression = 'infer')
        msg=Fore.GREEN+'Folder scanned and XLSX Files created successfully'+stat
    elif output_type==2:
        # msg=Fore.GREEN+"check json now"
        ## Created new dictionary and assigned existing dataframe as json child object by converting datarame to json
        # concatdata={"Folder_list":ls_fol,"Files_list":filtered_files}
        # print(dfc)
        concatdata={"Folder_list":dfc.to_json(),"Files_list":dfm.to_json(),"License_list":dfinfo.to_json()}
        with open(".\export_files\deepanalysis.json", "w") as outfile:
            json.dump(concatdata, outfile)
        msg=Fore.GREEN+'Folder(s) scanned and json File created successfully'+stat
    else:
        msg=Fore.RED+"No valid type was chosen."


    return msg
