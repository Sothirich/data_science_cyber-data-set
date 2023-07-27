# Danet

## Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


## Step 1 : Collect data

### reading data
df1=pd.read_csv('Data/Data_of_Attack_Back.csv')
df2=pd.read_csv('Data/Data_of_Attack_Back_BufferOverflow.csv')
df3=pd.read_csv('Data/Data_of_Attack_Back_FTPWrite.csv')
df4=pd.read_csv('Data/Data_of_Attack_Back_GuessPassword.csv')
df5=pd.read_csv('Data/Data_of_Attack_Back_NMap.csv')
df6=pd.read_csv('Data/Data_of_Attack_Back_Neptune.csv')
df7=pd.read_csv('Data/Data_of_Attack_Back_Normal.csv')
df8=pd.read_csv('Data/Data_of_Attack_Back_PortSweep.csv')
df9=pd.read_csv('Data/Data_of_Attack_Back_RootKit.csv')
df10=pd.read_csv('Data/Data_of_Attack_Back_Satan.csv')
df11=pd.read_csv('Data/Data_of_Attack_Back_Smurf.csv')

### add missing header to Data_of_Attack_Back_FTPWrite.csv
header = df1.columns
df3.columns = header

### add new column attack
df1['attack']=['data_of_attack_back']*df1.shape[0]
df2['attack']=['data_of_attack_back_BufferOverflow']*df2.shape[0]
df3['attack']=['data_of_attack_back_FTPWrite']*df3.shape[0]
df4['attack']=['data_of_attack_back_GuessPassword']*df4.shape[0]
df5['attack']=['data_of_attack_back_NMap']*df5.shape[0]
df6['attack']=['data_of_attack_back_Neptune']*df6.shape[0]
df7['attack']=['data_of_attack_back_Normal']*df7.shape[0]
df8['attack']=['data_of_attack_back_PortSweep']*df8.shape[0]
df9['attack']=['data_of_attack_back_RootKit']*df9.shape[0]
df10['attack']=['data_of_attack_back_Satan']*df10.shape[0]
df11['attack']=['data_of_attack_back_Smurf']*df11.shape[0]

### concate all the data to one file
df=pd.concat([df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11])
df.reset_index()

### export data to csv file
df.to_csv('Data/Data_of_Attack_Appends.csv', index=False)

### export to a variable
df = pd.read_csv('Data/Data_of_Attack_Appends.csv')
######################

## Step 2: Clean data

### clean Unnamed columns
df.columns[0]

### check for null value
df.isnull().sum()

### dropping rows with missing values
df.dropna(inplace=True)

### check duplicated row
df.duplicated().sum()

### drop duplicated row 
df.drop_duplicates(inplace=True)

### check data types
# df.dtypes
# df.columns
# df

### remove space in header
df.columns = df.columns.str.replace(' ', '')

### exporting cleaned data to csv file
df.to_csv('Data/Data_of_Attack_Appends_Clean.csv', index=False)

### exporting cleaned data to a variable
df = pd.read_csv('Data/Data_of_Attack_Appends_Clean.csv')
# df
######################