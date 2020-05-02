# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data = pd.read_csv(path)
data.rename(columns={"Total" : "Total_Medals"}, inplace=True)
data.head(10)


# --------------
#Code starts here
cond=[data['Total_Summer']>data['Total_Winter'],data['Total_Summer']<data['Total_Winter'],data['Total_Summer'].eq(data['Total_Winter'])]
values=['Summer','Winter','Both']
data['Better_Event']=np.select(cond,values)
#data["Better_Event"]=np.where( data.Total_Summer.eq(data.Total_Winter),"Both", np.where(data.Total_Summer.gt(data.Total_Winter),"Summer","Winter"))
print(data.head(5))
better_event=data["Better_Event"].value_counts().idxmax()
print(better_event)


# --------------
#Code starts here
top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
print(top_countries.head(3))
top_countries.drop(top_countries.tail(1).index,inplace=True)

print(top_countries.head(3))

#Function Definition
def top_ten(top_countries, column_name):
    country_list = []
    country_list=top_countries.nlargest(10,column_name)['Country_Name']
    return(country_list)

#Function Call
top_10_summer = list(top_ten(top_countries,"Total_Summer"))
top_10_winter = list(top_ten(top_countries,"Total_Winter"))
top_10 = list(top_ten(top_countries,"Total_Medals"))

common=[country for country in top_10_summer if country in top_10_winter and country in top_10]


# --------------
#Code starts here
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

summer_df.plot(kind="bar")
winter_df.plot(kind="bar")
top_df.plot(kind="bar")



# --------------
#Code starts here
summer_df["Golden_Ratio"] = summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio=max(summer_df['Golden_Ratio']) 
print(summer_max_ratio)
summer_country_gold=summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name']
print(summer_country_gold)

winter_df["Golden_Ratio"] = winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio=max(winter_df['Golden_Ratio']) 
print(winter_max_ratio)
winter_country_gold=winter_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name']
print(winter_country_gold)

top_df["Golden_Ratio"] = top_df['Gold_Total']/summer_df['Total_Medals']
top_max_ratio=max(top_df['Golden_Ratio']) 
print(top_max_ratio)
top_country_gold=top_df.loc[top_df['Golden_Ratio'].idxmax(),'Country_Name']
print(top_country_gold)



# --------------
#Code starts here
data_1=data[:-1]
print(data_1.head(3))
data_1['Total_Points']=data_1['Gold_Total']*3 + data_1['Silver_Total']*2 + data_1['Bronze_Total']*1
most_points=max(data_1['Total_Points'])
print(most_points)
best_country=data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']
print(best_country)


# --------------
#Code starts here
best=data[data['Country_Name']==best_country].head(1)

best=best[['Gold_Total','Silver_Total','Bronze_Total']]

best.plot.bar()
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation='45')


