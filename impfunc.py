
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
    filecount=0
    import os
    x = []
    for root, dirs, files in os.walk(path):
        for file in files:
            x.append(root+'\\'+file)
        # print(dirs)    
        filecount += len(files)             # counting files in each folder
    print('Number of files in directory is: ',filecount)
    return x


    

def countfiles_in_directory(path):          ## Not working
    import fnmatch
    import os
    dir_path = r'C:\Users\trevi\Downloads\Envato Components'
    count = len(fnmatch.filter(os.listdir(dir_path), '*.*'))
    print('File Count:', count)
    return count


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
        print("Number of files in this directory:",count)
    print("Number of folders : ",len(f))
    return f