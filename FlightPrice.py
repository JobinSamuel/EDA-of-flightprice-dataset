import pandas as pd
data = pd.read_excel("/Users/jobinsamuel/Desktop/DS New /DS/Data_Train.xlsx")
data.head()
data.info()
data.isnull().sum()
data.duplicated().sum()
data.describe()
# Converting date column
data['Day']= data['Date_of_Journey'].str.split('/').str[0]
data['Month'] = data['Date_of_Journey'].str.split('/').str[1]
data['Year'] = data['Date_of_Journey'].str.split('/').str[2]
data.head()
data.info()

data['Day'] = data['Day'].astype(int) #Siince the new features are object type convertingit to integer
data['Month'] = data['Month'].astype(int)
data['Year'] = data['Year'].astype(int)
data.info()

#Dropping the Date_of_Journey column
data = data.drop('Date_of_Journey',axis =1)
data.head()

# Working on Arrival_Time
#applyin lamda function to remove date from arrival time
data['Arrival_Time'] = data['Arrival_Time'].apply(lambda x: x.split(' ')[0])
data['Arrival_Hour'] = data['Arrival_Time'].str.split(':').str[0]
data['Arrival_Min'] =  data['Arrival_Time'].str.split(':').str[1]
data.head()

# dropping arrival time from the data
data = data.drop('Arrival_Time', axis= 1)
data.head()

# COnverting arrival hour and min to int
data['Arrival_Hour'] = data['Arrival_Hour'].astype(int)
data['Arrival_Min'] = data['Arrival_Min'].astype(int)
data.info()

data['Duration_hour'] = data['Duration'].str.extract(r'(\d+)h')[0].fillna('0')
data['Duration_min'] = data['Duration'].str.extract(r'(\d+)m')[0].fillna('0')
data.head()

data['Dep_hour'] = data['Dep_Time'].str.split(':').str[0]
data['Dep_min'] = data['Dep_Time'].str.split(':').str[1]
data['Dep_hour']= data['Dep_hour'].astype('int')
data['Dep_min'] = data['Dep_min'].astype('int')

data = data.drop('Dep_Time',axis = 1)
data = data.drop('Route',axis =1)
data = data.drop('Duration',axis =1)
print(data)

data['Additional_Info'].unique()

from sklearn.preprocessing import OneHotEncoder

ohe = OneHotEncoder()


nw = pd.DataFrame(ohe.fit_transform(data[['Airline','Source','Destination','Additional_Info']]).toarray(),columns=ohe.get_feature_names_out())

data_nw = pd.concat([data,nw],axis = 1)

print(data_nw)

data_nw = data_nw.drop(['Airline','Source','Destination','Additional_Info'],axis =1)

data_nw['Total_Stops'] = data_nw.Total_Stops.map({'non-stop' : 0, '2 stops': 2, '1 stop':1, '3 stops':3, '4 stops':4})

data_nw['Duration_hour']= data_nw['Duration_hour'].astype('int')
data_nw['Duration_min'] = data_nw['Duration_min'].astype('int')
data_nw.info()

