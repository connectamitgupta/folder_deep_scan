
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


###########################################

#### function to check whether directory is valid git repo or not
def is_git_repo(path):
    import git
    from git import Repo
    try:
        _ = git.Repo(path).git_dir
        return True
    except git.exc.InvalidGitRepositoryError:
        return False



    ######### V3 ###############

def list_files_in_directory_v3(path):
    # try:
    '''docstring for list_files_in_directory'''
    totalfilecount=0
    ### defiing constant for Git 
    gitremoterepopath="https://gitlab.com/trevita-envatoelements/set-8"
    import os
    
    #### List of directories
    ls_fol=list_directory(path)
    for x in ls_fol:
        print("folder object:",x)
        print("Base name of folder: ",os.path.basename(x))

    ### check git folder exists or not
    gitdir="gitoperation"
   
    gitdirpath = os.path.join(path, gitdir)
    import git
    from git import Repo
    gitremoterepopath="https://gitlab.com/trevita-envatoelements/set-8"

    if os.path.exists(gitdirpath):
        print("Folder exists",gitdirpath)
        tempxx = is_git_repo(gitdirpath)
        if tempxx==True:
            print("This is valid git directory",tempxx)
        elif tempxx==False:
            print("This is not a valid git directory",tempxx)

            print("Git remote default path is:",gitremoterepopath)
            grrp_check=input("Do you want to change in it(Yes/No): ")
            if ((grrp_check=='Yes') or (grrp_check=='Y') or (grrp_check=='y')):
                gitremoterepopath=input("Enter New Path: 1st ")
                ##pending validaion of input url valid or not

                Repo.clone_from(gitremoterepopath,gitdirpath)
            else:
                Repo.clone_from(gitremoterepopath,gitdirpath)    

    else:
        print("Need to create folder",gitdirpath)
        os.mkdir(gitdirpath)
        print("Directory '% s' created" % gitdir) 
        # import git
        # from git import Repo
        # gitremoterepopath="https://gitlab.com/Trevita/my-envato-2023"
        print("Git remote default path is:",gitremoterepopath)
        grrp_check=input("Do you want to change in it(Yes/No): ")
        if ((grrp_check=='Yes') or (grrp_check=='Y') or (grrp_check=='y')):
            gitremoterepopath=input("Enter New Path: 2nd")
            ##pending validaion of input url valid or not
            print("You enter value is :",gitremoterepopath)
            # grrp_path_check=git.execute(f"git ls-remote {gitremoterepopath}")
            # print("grrp_path_check",grrp_path_check) 
            Repo.clone_from(gitremoterepopath,gitdirpath)
        else:
            Repo.clone_from(gitremoterepopath,gitdirpath)
        
    repo=git.Repo(gitdirpath)
    # repo.git.pull()
    pp3=repo.git.execute("git fetch --all")
    print("git fetch executed : ",pp3)

    # repo = git.Repo(".", search_parent_directories=True) 
    print ("Location "+ repo.working_tree_dir)
    print ("Remote: " + repo.remote("origin").url)
    ga=repo.git.status()
    print(ga)



    #### for git 1
    # import git
    # repo_url = "https://gitlab.com/Trevita/my-envato-2023"
    # local_path = path+'/new'
    # repo = git.Repo.clone_from(repo_url, path)
    ### for git 2
    # from git import Repo
    # # repo = Repo('path/to/git/repo')  # if repo is CWD just do '.'
    # repo=Repo(path)
    #     # Reference https://stackoverflow.com/questions/41836988/git-push-via-gitpython
    ### for git 3
    # import git
    # from git import Repo
    # # Repo.clone_from("https://gitlab.com/Trevita/my-envato-2023",path)
    # repo=git.Repo(gitdirpath)
    # ga=repo.git.execute("git status")
    # print(ga)
    # Raises InvalidGitRepositoryError when not in a repo
  
       
    # repo.git.pull()
    # Pathnm = os.path.basename(gitdirpath)
    # print("Pathname is : ",Pathnm)
    ### Python code here creating list
    x1 = []
    x2 = []
    ### Going through loop for each folder
    for root, dirs, files in os.walk(path):
        ## initialize important type count to zero for each folder
        zipcount=0
        txtcount=0
        jpgcount=0
        pngcount=0
        licensecount=0
        pdfcount=0
        othercount=0
        #### git block 1
        # dname=os.path.dirname(path)
        ### https://www.geeksforgeeks.org/automating-some-git-commands-with-python/
        ### https://github.com/gitpython-developers/GitPython/issues/615
        # new_branch = repo_url.create_head(dname)
        # new_branch.checkout()
        ##### git block 3
        # if dname==os.path.dirname(path):
        # dname=os.walk(root)
        # print("Now root name is : ",root)
        # p=os.path.dirname(root)
        # print(p)
        # folderName = os.path.split(os.path.split(root)[0])[2]
        # folderName = os.path.split(root)[0]
        # folderName = os.path.dirname(root)
        folderName = os.path.basename(root)
        print("*********** Now checkig for folder  : ",folderName)

        # pp=os.getcwd(root)
        # print("OS PWD : ",pp)
        # from pathlib import Path
        # p = Path("/a/b/c/d/e.txt")
        # p.parts


        if root not in ls_fol:
            print(f"Super Condition 1 matched for folder {folderName} so skipping it")
            continue


        
        ### Skipping root(same) folder content and .git folder
        if '.git' in root:
            print(f"Condition 1 matched for folder {folderName} so skipping it")
            continue
        elif folderName == gitdir:
            print(f"Condition 2 matched for folder {folderName} so skipping it")
            continue
        elif 'test' in folderName:
            print(f"Condition 3 matched for folder {folderName} so skipping it")
            continue

        # for root, dirs, files in os.walk(path):
        localbranchname=folderName
        remotebranchname='origin/'+folderName
        print("checking for current folder remote Name is: ", remotebranchname)
        ### check if branch exists or not on remote
        localbranchexists=False
        remotebranchexists=False
        for ref in repo.references:
            # print("Branch Name is: ", ref.name)
            if remotebranchname == ref.name:
        # print("Branches names:",repo.references)
        # if remotebranchname in repo.references:
                remotebranchexists=True
                print("Remote Branch exists at",ref.name)
                # continue
            else:
                pass

            if localbranchname == ref.name:
                localbranchexists=True
                print("Local Branch exists at",ref.name)
            else:
                pass
                # print("Remote Branch does not exists",remotebranchname)
                # continue
                # branchexists=False
            # print("Remote Branch name to check is: ",remotebranchname)

        ## Ref https://stackoverflow.com/questions/50707781/gitpython-how-to-check-if-a-remote-branch-exists

        # if remotebranchname == ref.name:
        if remotebranchexists:
            print(f"{folderName} Branch exists at:")
            y1=repo.git.execute(f"git checkout {folderName}")
            print(f"git checkout to existing branch folder: {folderName} : ",y1)
            y2=repo.git.execute(f"git pull origin {folderName}")
            print(f"git checkout to existing branch folder: {folderName} : ",y2)
        
        elif localbranchexists:
            print(f"{folderName} Local Branch exists:")
        
        elif ((remotebranchexists==False) and (localbranchexists==False)):
            print(f"{folderName} Branch does not xists at:")
            y1=repo.git.execute(f"git checkout --orphan {folderName}")
            print(f"git checkout orphan executed for folder: {folderName} : ",y1)
            y2=repo.git.execute(f"git rm --cached -r .")
            print(f"git remove executed for branch: {folderName} : ",y2)
            y3=repo.git.execute("git clean -fd")
            print("git clean executed : ",y3)
            y4 = repo.git.execute('''git commit --allow-empty -m "Initial commit on orphan branch"''')
            print("git commit executed on orphan branch: ",y4)
    

        # y1a = repo.git.execute(f"git ls-remote --exit-code --heads origin ${folderName}")
        # print("Branch status: ",y1a)


        # # git checkout --orphan folderName
        # y1=repo.git.execute(f"git checkout --orphan {folderName}")
        # print(f"git checkout orphan executed for folder: {folderName} : ",y1)
        # # git rm --cached -r .
        # y2 = repo.git.execute("git rm --cached -r .")
        # print("git cache removed : ",y2)
        # # git clean -fd
        # y3=repo.git.execute("git clean -fd")
        # print("git clean executed : ",y3)
        
        # # git commit --allow-empty -m "Initial commit on orphan branch"
        # y4 = repo.git.execute('''git commit --allow-empty -m "Initial commit on orphan branch"''')
        # print("git commit executed on orphan branch: ",y4)
        # # git push -u origin <new branch>
        # y5 = repo.git.execute(f"git push -u origin {folderName}")
        # print("git pushed initially for this folder ",y5)
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
            ###### git block
            ## add file for git 1
            # repo.index.add([file])
            # print(f'Files {file} Added Successfully')
            # mg=f'file {file} added in repo'
            # repo.index.commit(mg)
            # print('Commited successfully')
            # origin = repo.remote(name='origin')
            # origin.push()
            # print('Pushed changes to origin')

            ##### git 2
            # repo.index.add(['bla.txt'])
            # repo.index.add([file])
            # print(f'Files {file} Added Successfully')
            # repo.index.commit(f'{file} added')
            # origin = repo.remote('origin')
            # import time
            # time.sleep(10)
            

            #### Copy files from source to destination folder
            sorc_file=(os.path.abspath(os.path.join(root, file)))
            print("Source file: ",sorc_file)
            dest_file=(os.path.abspath(os.path.join(gitdirpath, file)))
            print("Destination file: ",dest_file)
            
            import shutil
            if os.path.isfile(dest_file):
                print('File already exists, so skipping it', file)
                continue
            else:
                shutil.copy(sorc_file, dest_file)
                if os.path.isfile(dest_file):
                    print('copied', file)

                                ##### git 3
           
                    y6=repo.git.execute(f'git add "{dest_file}"')
                    print("y6: ",y6)
                    y7=repo.git.execute(f'''git commit --allow-empty -m "file added {file} on branch {folderName}"''')
                    print("y7: ",y7)
                    y8=repo.git.execute(f"git push origin {folderName}")
                    print("y8: ",y8)

            ##### git 3
            
            # y6=repo.git.execute(f'git add "{dest_file}"')
            # print("y6: ",y6)
            # y7=repo.git.execute(f'''git commit --allow-empty -m "file added {file} on branch {folderName}"''')
            # print("y7: ",y7)
            # y8=repo.git.execute(f"git push origin {folderName}")
            # print("y8: ",y8)
        
            ## folder info
            from pathlib import Path
            # p = Path("/a/b/c/d/e.txt")
            p = Path(file)
            print("parts of folder : ",p.parts)


        
        # print(root, "          ", zipcount,"          ",txtcount,"          ",licensecount,"          ",jpgcount,"          ",pngcount)
        ## creating object and appending extended information for each folder
        x1.append(folderdetcount(root,zipcount,txtcount,jpgcount,pngcount,licensecount,pdfcount,othercount))
    # except:
    #     x1={}
    #     x2={}

    return x1,x2


