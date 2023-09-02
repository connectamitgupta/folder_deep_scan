############################# Created by AMIT GUPTA ######################################################
import impfunc                             ## import function file


## Get all files in directory
files = impfunc.list_files_in_directory('D:\\Personal2023\\Phone Number\\Raw\Whatsapp - WIP')    ## define directory

## get filterered files only txt extension files
filtered_files = [i for i in files if '.txt' in i]

## Read all files one by one through this loop
# dfs = []                                   ### initialize new list
record={}                                    ###initialize a dictonary
i=1
for file in filtered_files:
#   df = pd.read_csv(file,sep='\t')
    # df=impfunc.licensereadbulk(file)       ### Use custom function to extract data from files
    import pandas as pd

    # df=pd.read_csv(file, thousands=r',')       ### Use panda read csv file with comma deliited
    # df=pd.read_csv(file, sep=',', header =None,names=['Mobile','File_name']).transpose()       ### Use panda read csv file with comma deliited
    df=pd.read_csv(file, sep=',',header=None)       ### Use panda read csv file with comma deliited
    print("Reading File....",file)
    df=df.T
    df.columns=["Mobile"]
    # data={"mobile":df[0]}
    # dfnew = pd.DataFrame(data,columns=list('abc'))
    # 
    # dfnew = pd.DataFrame(df)
    
    # dfnew['mobile'] = dfnew.index
    
    # df.assign(sourcename=file) 
    # print(dfnew)
    df['Fl'] = pd.Series([file for x in range(len(df.index))])


    # record.update({i:df})
    # print(record)
    # dfs.append(record)                      ### append list item 
    
    # print(type(df))
    # print(df.columns)
    # print(df.loc[0,1])
    # print(df)
    df.to_csv('phone.csv', mode='a', index=False, header=False)
    
    
    record[i]=pd.DataFrame(df)
    
    i+=1

# print(record)
print(type(record))
print(record.keys())
print(len(record))
# using item() to extract key value pair as whole
temp="Mobile"
res = [val[temp] for key, val in record.items() if temp in val]
# print("Extracted numbers are:",res)
print(type(res))
print(len(res))

print(record.get('1', {}).get('Mobile'))

df = pd.DataFrame(res) 
df.to_csv("phonethroughpanda.csv", index=False)