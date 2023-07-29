# Danet

## Importing libraries
import pandas as pd

## If you are NOT using Google Colab, comment out the following lines
from google.colab import drive
drive.mount('/content/drive')

## Step 1 : Collect data

### For testing only
additional_path = ''

### reading data
df1=pd.read_csv(additional_path + 'Data/Data_of_Attack_Back.csv')
df2=pd.read_csv(additional_path + 'Data/Data_of_Attack_Back_BufferOverflow.csv')
df3=pd.read_csv(additional_path + 'Data/Data_of_Attack_Back_FTPWrite.csv')
df4=pd.read_csv(additional_path + 'Data/Data_of_Attack_Back_GuessPassword.csv')
df5=pd.read_csv(additional_path + 'Data/Data_of_Attack_Back_NMap.csv')
df6=pd.read_csv(additional_path + 'Data/Data_of_Attack_Back_Neptune.csv')
df7=pd.read_csv(additional_path + 'Data/Data_of_Attack_Back_Normal.csv')
df8=pd.read_csv(additional_path + 'Data/Data_of_Attack_Back_PortSweep.csv')
df9=pd.read_csv(additional_path + 'Data/Data_of_Attack_Back_RootKit.csv')
df10=pd.read_csv(additional_path + 'Data/Data_of_Attack_Back_Satan.csv')
df11=pd.read_csv(additional_path + 'Data/Data_of_Attack_Back_Smurf.csv')

### add missing header to Data_of_Attack_Back_FTPWrite.csv
header = df1.columns
df3.columns = header

### Converting attack names to numbers
## Normal = 0, Back = 1, BufferOverflow = 2, FTPWrite = 3, GuessPassword = 4, NMap = 5, Neptune = 6, PortSweep = 7, RootKit = 8, Satan = 9, Smurf = 10

### add new column attack
df1['attack']= [1] * df1.shape[0]
df2['attack']= [2] * df2.shape[0]
df3['attack']= [3] * df3.shape[0]
df4['attack']= [4] * df4.shape[0]
df5['attack']= [5] * df5.shape[0]
df6['attack']= [6] * df6.shape[0]
df7['attack']= [0] * df7.shape[0]
df8['attack']= [7] * df8.shape[0]
df9['attack']= [8] * df9.shape[0]
df10['attack']= [9] * df10.shape[0]
df11['attack']= [10] * df11.shape[0]

### concate all the data to one file
df=pd.concat([df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11])
df.reset_index()

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
df.to_csv(additional_path + 'Data/Data_of_Attack_Appends_Clean.csv', index=False)

### exporting cleaned data to a variable
df = pd.read_csv(additional_path + 'Data/Data_of_Attack_Appends_Clean.csv')
# df

######################