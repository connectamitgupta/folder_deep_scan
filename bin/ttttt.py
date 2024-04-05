import pandas as pd
exceldataDF=pd.read_excel(r"C:\Users\Dell\Downloads\Your Portfolio Transactions Statement-A705876 (2).xlsx")
exceldataDF.dropna()
# exceldataDF

p1= exceldataDF[exceldataDF['Angel One Limited']=='Your Current Holdings'].index.values   ### finding position for current holding begin
p2= exceldataDF[exceldataDF['Angel One Limited']=='Your Past Transactions'].index.values   ### finding position for current holding begin

basicInfoDF=exceldataDF.iloc[0:p1[0]-1,0:2]
basicInfoDF=basicInfoDF.T
# basicInfoDF

# txnDataIndex=exceldataDF.iloc[p1[0]+1]
# txnDataIndex
## Assign columns proper names
txnDataDF=exceldataDF.iloc[p1[0]+1:,:]
txnDataDF.columns=txnDataIndex=exceldataDF.iloc[p1[0]+1]

# txnDataDF=txnDataDF.drop(12)          ############ Problem exists here
## Add columns and update data
txnDataDF['TxnStatus']='Past'
ss=txnDataDF.shape
txnDataDF.TxnStatus[:(p2[0]-1)-(p1[0]+1)]='Current'

## Remove unwanted columns
# txnDataDF=txnDataDF.drop([p1[0]+1,p2[0],p2[0]+1])          ############ Problem exists here
txnDataDF = txnDataDF.drop([p2[0],p2[0]+1])
# txnDataDF.drop('20')          ############ Problem exists here
# txnDataDF

### Removing rows where NaN exists in Qty columns
txnDataDF=txnDataDF[txnDataDF['Qty'].notna()]
txnDataDF