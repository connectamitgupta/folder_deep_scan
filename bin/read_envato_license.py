import impfunc                             ## import function file


############################# Created by AMIT GUPTA ######################################################
################# Version 1 program
def menuchosen_v1():


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
    with open('.\export_files\exportthroughnative.csv', 'a', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(dfs)


    ## Save CSV using pandas method
    import pandas as pd
    df = pd.DataFrame(dfs) 
    df.to_csv(".\export_files\exportthroughpanda.csv", index=False, mode='a', header=False)

    ## Save Excel using pandas method
    import pandas as pd
    # print(dfs)
    ### converting list to pandas dataframes
    df = pd.DataFrame(dfs)
    filtered_files=pd.DataFrame(filtered_files)
    ls_fol=pd.DataFrame(ls_fol)
    # print(l)
    # create a excel writer object
    with pd.ExcelWriter(".\export_files\exportthroughpanda.xlsx") as writer:
        ls_fol.to_excel(writer, sheet_name='Folder_list', index=False)
        filtered_files.to_excel(writer, sheet_name='Files_list', index=False)
        df.to_excel(writer, sheet_name='License_list', index=False)
        # dfn.to_excel(writer, sheet_name='Folder_details', index=False)
        

    # with pd.ExcelWriter(".\exportthroughpanda.xlsx",mode='a') as writer:
        # ls_fol.to_excel(writer, sheet_name='Folder_list',if_sheet_exists = 'overlay', index=False)
        # filtered_files.to_excel(writer, sheet_name='Files_list',if_sheet_exists = 'overlay', index=False)
        # df.to_excel(writer, sheet_name='License_list',if_sheet_exists = 'overlay', index=False)
    return "Folder scanned and File created successfully"
###################################################################################################
#################################### V2 ###########################################################
from tkinter import filedialog
from tkinter import *
def menuchosen_v2():

    ############ Asking user to select folder for execution ##################
    # from tkinter import filedialog
    # from tkinter import *
    root = Tk()
    # root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    # print (root.filename)
    folder_path = filedialog.askdirectory()
    print ("You have chosen folder to scan: ",folder_path)

    ### Getting Folders and file names throough function and get multiple objects
    dfc, dfm=impfunc.list_files_in_directory_new(folder_path)
    import pandas as pd
    # dft = pd.DataFrame([x.as_dict() for x in fl])
    
    ### all files information and seperate object columns and save as dataframe
    dfm = pd.DataFrame([vars(d) for d in dfm])
        # print(dfm)

    ## Getting only files from all folders
    files = impfunc.list_files_in_directory(folder_path)    ## define directory



    ## get filterered files only txt extension files
    filtered_files = [i for i in files if '.txt' in i]
    print(filtered_files)

    ## Read all files one by one through this loop
    dfs = []                                ### initialize new list
    for file in filtered_files:
        # print(file)
    #   df = pd.read_csv(file,sep='\t')
        a=impfunc.licensereadbulk(file)       ### Use custom function to extract data from files
        # print(df)
        dfs.append(a)                      ### append list item 
    # print(type(dfs))



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

    ### Converting list of objects  to pandas dataframe
    ### folder information seperate object columns and save as dataframe
    dfc=pd.DataFrame([vars(d) for d in dfc])
    # print(dfc)

    ### all files information and seperate object columns and save as dataframe
    # dfm = pd.DataFrame([vars(d) for d in dfm])
        # print(dfm)

    ### deep scanned file info all info 
    dfinfo=pd.DataFrame(dfs)


    with pd.ExcelWriter(".\export_files\india.xlsx") as writer:
        dfc.to_excel(writer, sheet_name='Folder_information', index=False, header=True)
        dfm.to_excel(writer, sheet_name='Files_information', index=False, header=True)
        dfinfo.to_excel(writer, sheet_name='DeepFileinformation', index=False, header=True)

    # dfc.to_json('file1.json', orient = 'split', compression = 'infer')

    return 'Folder scanned and XLSX Files created successfully'