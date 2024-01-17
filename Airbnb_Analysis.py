**INSTALLING PYMONGO**

!pip install pymongo

**IMPORTING ALL NECESSARY LIBRARIES**

import pandas as pd
import numpy as np
import statistics as st
import matplotlib.pyplot as plt
import seaborn as sns
from pymongo import MongoClient


**RETRIEVING DATA FROM MONGODB ATLAS**

connection_string = "mongodb+srv://soniyasurendhar:1234@cluster0.psa1gyo.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(connection_string)
db = client.sample_airbnb
collection = db.listingsAndReviews

data = []
for i in collection.find():
  data.append(i)

airbnb = pd.DataFrame(data)

airbnb.to_csv('airbnb.csv',index=False)

airbnb_1 = pd.read_csv("airbnb.csv")

airbnb_1

airbnb_1.shape

airbnb_1.columns

**CHECKING AND HANDLING MISSING VALUES**

airbnb_1.isnull().sum()

#looking for the percentage of missing values
pd.DataFrame(airbnb_1.isna().mean()*100).T

#dropping the columns  missing values
airbnb_1.drop(columns=['neighborhood_overview','notes','transit','access','interaction','house_rules','first_review','last_review','weekly_price','monthly_price','reviews_per_month'],inplace = True)

#imputing median value for the column"bedrooms","beds","bathrooms","security_deposit","cleaning_fee" because it has outliers
airbnb_1['bedrooms'].fillna(airbnb_1['bedrooms'].median(),inplace = True)
airbnb_1['beds'].fillna(airbnb_1['beds'].median(),inplace = True)
airbnb_1['bathrooms'].fillna(airbnb_1['bathrooms'].median(),inplace = True)
airbnb_1['security_deposit'].fillna(airbnb_1['security_deposit'].median(),inplace = True)
airbnb_1['cleaning_fee'].fillna(airbnb_1['cleaning_fee'].median(),inplace = True)

airbnb_1 = airbnb_1.dropna()

airbnb_1.shape

airbnb_1.isnull().sum()

 **DATATYPE CORRECTION**

airbnb_1.dtypes

#converting the datatype into right format
airbnb_1['bedrooms'] = airbnb_1['bedrooms'].astype(int)
airbnb_1['beds'] = airbnb_1['beds'].astype(int)
airbnb_1['bathrooms'] = airbnb_1['bathrooms'].astype(int)
airbnb_1['extra_people'] = airbnb_1['extra_people'].astype(int)
airbnb_1['price'] = airbnb_1['price'].astype(int)
airbnb_1['cleaning_fee'] = airbnb_1['cleaning_fee'].astype(int)
airbnb_1['security_deposit'] = airbnb_1['security_deposit'].astype(int)

airbnb_1.dtypes

int_data_cols = [i for i in airbnb_1.columns if airbnb_1[i].dtypes == "int64"]
int_data_cols

object_data_cols = [i for i in airbnb_1.columns if airbnb_1[i].dtypes == "object"]
object_data_cols

# **CHECKING FOR OUTLIERS**

airbnb_1.describe()

Q1 = airbnb_1['minimum_nights'].quantile(0.25)
Q3 = airbnb_1['minimum_nights'].quantile(0.75)
IQR = Q3-Q1
print(IQR)
lower_bound = Q1 - (1.5*IQR)
upper_bound = Q3 + (1.5*IQR)
print(lower_bound,upper_bound)

#column 'minimum_nights' has outlier so clipping the outliers
airbnb_1['minimum_nights'] = airbnb_1['minimum_nights'].clip(upper_bound,lower_bound)

Q1 = airbnb_1['maximum_nights'].quantile(0.25)
Q3 = airbnb_1['maximum_nights'].quantile(0.75)
IQR = Q3-Q1
print(IQR)
lower_bound = Q1 - (1.5*IQR)
upper_bound = Q3 + (1.5*IQR)
print(lower_bound,upper_bound)

#no ouliers in the column 'maximum_nights'

Q1 = airbnb_1['accommodates'].quantile(0.25)
Q3 = airbnb_1['accommodates'].quantile(0.75)
IQR = Q3-Q1
print(IQR)
lower_bound = Q1 - (1.5*IQR)
upper_bound = Q3 + (1.5*IQR)
print(lower_bound,upper_bound)

#column 'accomadates' has outlier we have to clip
airbnb_1['accommodates'] = airbnb_1['accommodates'].clip(upper_bound,lower_bound)

Q1 = airbnb_1['bedrooms'].quantile(0.25)
Q3 = airbnb_1['bedrooms'].quantile(0.75)
IQR = Q3-Q1
print(IQR)
lower_bound = Q1 - (1.5*IQR)
upper_bound = Q3 + (1.5*IQR)
print(lower_bound,upper_bound)

#column 'bedrooms'has outlier we have to clip it
airbnb_1['bedrooms'] = airbnb_1['bedrooms'].clip(upper_bound,lower_bound)

Q1 = airbnb_1['beds'].quantile(0.25)
Q3 = airbnb_1['beds'].quantile(0.75)
IQR = Q3-Q1
print(IQR)
lower_bound = Q1 - (1.5*IQR)
upper_bound = Q3 + (1.5*IQR)
print(lower_bound,upper_bound)

#column 'beds' has outlier we have to clip it
airbnb_1['beds'] = airbnb_1['beds'].clip(upper_bound,lower_bound)

Q1 = airbnb_1['number_of_reviews'].quantile(0.25)
Q3 = airbnb_1['number_of_reviews'].quantile(0.75)
IQR = Q3-Q1
print(IQR)
lower_bound = Q1 - (1.5*IQR)
upper_bound = Q3 + (1.5*IQR)
print(lower_bound,upper_bound)

#column "number_of_reviews" has outliers we have to clip
airbnb_1['number_of_reviews'] = airbnb_1['number_of_reviews'].clip(upper_bound,lower_bound)

Q1 = airbnb_1['bathrooms'].quantile(0.25)
Q3 = airbnb_1['bathrooms'].quantile(0.75)
IQR = Q3-Q1
print(IQR)
lower_bound = Q1 - (1.5*IQR)
upper_bound = Q3 + (1.5*IQR)
print(lower_bound,upper_bound)

#column "bathrooms" has outliers we have to clip
airbnb_1['bathrooms'] = airbnb_1['bathrooms'].clip(upper_bound,lower_bound)

Q1 = airbnb_1['price'].quantile(0.25)
Q3 = airbnb_1['price'].quantile(0.75)
IQR = Q3-Q1
print(IQR)
lower_bound = Q1 - (1.5*IQR)
upper_bound = Q3 + (1.5*IQR)
print(lower_bound,upper_bound)

#column "price" has outliers we have to clip
airbnb_1['price'] = airbnb_1['price'].clip(upper_bound,lower_bound)

Q1 = airbnb_1['security_deposit'].quantile(0.25)
Q3 = airbnb_1['security_deposit'].quantile(0.75)
IQR = Q3-Q1
print(IQR)
lower_bound = Q1 - (1.5*IQR)
upper_bound = Q3 + (1.5*IQR)
print(lower_bound,upper_bound)

#column "security_deposit" has outliers we have to clip
airbnb_1['security_deposit'] = airbnb_1['security_deposit'].clip(upper_bound,lower_bound)

Q1 = airbnb_1['cleaning_fee'].quantile(0.25)
Q3 = airbnb_1['cleaning_fee'].quantile(0.75)
IQR = Q3-Q1
print(IQR)
lower_bound = Q1 - (1.5*IQR)
upper_bound = Q3 + (1.5*IQR)
print(lower_bound,upper_bound)

#column "cleaning_fee" has outliers we have to clip
airbnb_1['cleaning_fee'] = airbnb_1['cleaning_fee'].clip(upper_bound,lower_bound)

Q1 = airbnb_1['extra_people'].quantile(0.25)
Q3 = airbnb_1['extra_people'].quantile(0.75)
IQR = Q3-Q1
print(IQR)
lower_bound = Q1 - (1.5*IQR)
upper_bound = Q3 + (1.5*IQR)
print(lower_bound,upper_bound)

#column "extra_people" has outliers we have to clip
airbnb_1['extra_people'] = airbnb_1['extra_people'].clip(upper_bound,lower_bound)

Q1 = airbnb_1['guests_included'].quantile(0.25)
Q3 = airbnb_1['guests_included'].quantile(0.75)
IQR = Q3-Q1
print(IQR)
lower_bound = Q1 - (1.5*IQR)
upper_bound = Q3 + (1.5*IQR)
print(lower_bound,upper_bound)

#column "guests_included" has outliers we have to clip
airbnb_1['guests_included'] = airbnb_1['guests_included'].clip(upper_bound,lower_bound)

airbnb_1.describe()

**CHECKING FOR DUPLICATES**

airbnb_1.duplicated().sum()#no duplicates

airbnb_1.shape

airbnb_cleaned = pd.DataFrame(airbnb_1)

airbnb_cleaned.to_csv("airbnb_cleaned.csv")

airbnb_cleaned.shape

# **POWERBI DASHBOARD**

PowerBI dashboard is given as pdf format

**OUR ANALYSIS**
* The price increases as the extra people increases
* The price increases as the no of AMENITIES increases
* The price increases as the no of BED increases
* In property type APARTMENT has more price
* In room type ENTIRE ROOM has more price
* MARCH month has more price comparitively to other months
* The MINIMUM NIGHT is 1 and the MAXIMUM NIGHT is 1125
* As the Ratings increased Price also increases

