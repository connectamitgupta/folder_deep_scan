
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
        record={}                               ## initialize new dictionary
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
                    record.update({ky:val})         ## Update dicionary with new key, value pair
                    i+=1
    # record=[record]
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




###################################################################################################
#################################### V2 ###########################################################


class filedet:
    def __init__(self, loc, fname):
        self.location = loc
        self.name = fname
        # print(self.location)
        # print(self.name)

 
def list_files_in_directory_new(path):
    '''docstring for list_files_in_directory'''
    totalfilecount=0
    import os
    # Python3 code here creating class
   
    x1= []
    for root, dirs, files in os.walk(path):
        zipcount=0
        txtcount=0
        jpgcount=0
        pngcount=0
        licensecount=0
        for file in files:
            # filelist={}
            # filelist={file,root}
            # filelist.add('location',root)
            # x.append(root+'\\'+file)
            
            if '.zip' in file:
                zipcount+=1

            if '.txt' in file:
                txtcount+=1

            if '.txt' and 'license_certificate' in file:
                licensecount+=1
                

            if '.jpg' in file:
                jpgcount+=1

            if '.png' in file:
                pngcount+=1

            # zipcount = lambda zipcount : zipcount+1 if('.zip' in file) else None
            # txtcount = lambda txtcount : txtcount+1 if('.txt' in file) else None
            x1.append(filedet(root,file))
        print(root, "          ", zipcount,"          ",txtcount,"          ",licensecount,"          ",jpgcount,"          ",pngcount)

            # x1.append(filelist)
            
            # print(root,"Sub-directorties are: ",dirs)    
        # filecount += len(files)             # counting files in each folder
        # print('Number of files in directory is: ',filecount)
    # totalfilecount += filecount
    # print('Total file count is :',totalfilecount)
    return x1