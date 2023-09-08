
from colorama import Fore

def licenseread():                              ### Useful for static file

    filename = "D:\\tempp\\Django_Admin_Panel\license_certificate_3C9MY2EG6D.txt"
    substring=("Item Title", "Item URL",
    "Item ID",
    "Author Username",
    "Licensee",
    "Registered Project Name",
    "License Date",
    "Item License Code"     
    )                                                   ## created tuple for required fieldname 


    plen=len(substring)-1
    i=0

    with open(filename, "r") as file:
        record={}
        for x in file:
            for subs in substring:
                lnlen=len(x)
                if i>plen:
                    break
                # print(f"value of i is {i}")
                txt=substring[i]
                if txt in x:
                    len(substring[i])
                    # print(x)
                    # print(lnlen)
                    # print(len(substring[i]))
                    m=len(substring[i])+1
                    # print(x[m:])
                    n=x[m:]
                    val=n.strip()
                    # print(len(val))
                    # print(val)
                    ky=substring[i]
                    # print(ky)
                    record.update({ky:val})
                    i+=1

    print(type(record))
    print(record)

    print(type(record))
    record=[record]
    file.close()


# licenseread()



def licensereadbulk(file):              ### Useful for dynamic file

    filename = file
    substring=("Item Title", "Item URL",
    "Item ID",
    "Author Username",
    "Licensee",
    "Registered Project Name",
    "License Date",
    "Item License Code"     
    )                                                   ## created tuple for required fieldname 


    plen=len(substring)-1
    i=0

    with open(filename, "r") as file:
        record={}                              ## initialize new dictionary
        ## Update file name in dictionary 
        record.update({"file_name":filename})
        ## Scanning through file
        for x in file:
            ## iteration for searching required text from tuple which is set of required parameters of license
            for subs in substring:
                lnlen=len(x)
                if i>plen:
                    break
                # print(f"value of i is {i}")
                txt=substring[i]
                if txt in x:
                    len(substring[i])
                    # print(x)
                    # print(lnlen)
                    # print(len(substring[i]))
                    m=len(substring[i])+1
                    # print(x[m:])
                    n=x[m:]
                    val=n.strip()
                    # print(len(val))
                    # print(val)
                    ky=substring[i]
                    # print(ky)
                    record.update({ky:val})         ## Update dicionary with new key, value pair
                    i+=1
 
    return record
    file.close()



def list_files_in_directory(path):
    '''docstring for list_files_in_directory'''
    totalfilecount=0
    import os
    x = []
    for root, dirs, files in os.walk(path):
        filecount=0
        for file in files:
            x.append(root+'\\'+file)
        # print(root,"Sub-directorties are: ",dirs)    
        filecount += len(files)             # counting files in each folder
        # print('Number of files in directory is: ',filecount)
    # totalfilecount += filecount
    # print('Total file count is :',totalfilecount)
    return x






def list_directory(path): 
    import os
    f = []
    rootdir = 'path/to/dir'
    for it in os.scandir(path):
        count=0
        if it.is_dir():
            # print(it.path)
            f.append(it.path)

        if it.is_file():
            count += 1
    # print("Number of files in this subdirectory:",count)
    # print("Number of folders : ",len(f))
    return f

####### Main menu functions #######################################
#### fucntion to get numeric inputs 
def numInput(a): 
    number = input(f"\tEnter {a} number: ") 
    if number.isdigit(): 
        return int(number) 
    else: 
        print (Fore.RED+"You must enter a number (i.e. 0,1,2...)" )
        numInput(a)

### function to get output type in main menu
def output_format():
    # if choice==1 or choice==2:
    print(Fore.BLUE+'''
        __________________________________________________________________________________________
        ******************** What do you want to generate XLSX or CSV or json ********************
        A. XLSX                                           ....[1]
        B. Json                                           ....[2]
        ''')
    
    typec = numInput("output choice")
    return typec



###################################################################################################
#################################### V2 ###########################################################


class filedet:
    def __init__(self, loc, fname):
        self.folder_location = loc
        self.file_name = fname
        # print(self.location)
        # print(self.name)

class folderdetcount:
    def __init__(self,path,zipc,txtc,jpgc,pngc,licensec,pdfc,otherc):
        # self.location = loc
        self.folder_location = path
        self.zip_count = zipc
        self.txt_count = txtc
        self.jpg_count = jpgc
        self.png_count = pngc
        self.license_count = licensec
        self.pdf_count = pdfc
        self.other_count = otherc

    def info(self):
        # return f"Folder name is: {self.name} "
        return self.file_name

    def count(self):
        print(f"zip files are: {self.zipcount}")
        print(f"txt files are: {self.txtcount}")
        print(f"jpg files are: {self.jpgcount}")
        print(f"png files are: {self.pngcount}")
        print(f"license files are: {self.licensecount}")
        print(f"pdf files are: {self.pdfcount}")
    
    def columns_info(self):
        cn=["path","zip count","txt count","jpg count","png count","license count","pdf count"]
        return(cn)

 
def list_files_in_directory_new(path):
    '''docstring for list_files_in_directory'''
    totalfilecount=0
    import os
    ### Python code here creating list
    x1 = []
    x2 = []
    ### Going through loop for each folder
    for root, dirs, files in os.walk(path):
        ## initialize importnat type count to zero for each folder
        zipcount=0
        txtcount=0
        jpgcount=0
        pngcount=0
        licensecount=0
        pdfcount=0
        othercount=0
        for file in files:
            # counting each file 
            if '.zip' in file:
                zipcount+=1
            elif '.txt' in file:
                txtcount+=1
            elif '.txt' and 'license_certificate' in file:
                licensecount+=1
            elif '.jpg' in file:
                jpgcount+=1
            elif '.jpeg' in file:
                jpgcount+=1
            elif '.png' in file:
                pngcount+=1
            elif '.pdf' in file:
                pdfcount+=1
            else:
                othercount+=1

            ## creating object and appending object to filelist class for folder and files inside
            x2.append(filedet(root,file))
        # print(root, "          ", zipcount,"          ",txtcount,"          ",licensecount,"          ",jpgcount,"          ",pngcount)
        ## creating object and appending extended information for each folder
        x1.append(folderdetcount(root,zipcount,txtcount,jpgcount,pngcount,licensecount,pdfcount,othercount))
        
    return x1,x2