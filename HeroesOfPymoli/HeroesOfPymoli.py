import pandas as pd
import os

# File to Load (Remember to Change These)
file_to_load = os.path.join(".", "Desktop", "pandas-challenge", "HeroesOfPymoli", "Resources", "purchase_data.csv")

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)


##PLAYER COUNT
#Unique players plus their count:
count_unique_players_df = len(purchase_data["SN"].unique())#returns count of times a unique item
print(count_unique_players_df)


##PURCHASING ANALYSIS (TOTAL)
#Number of Unique Items:
count_unique_items_df = len(purchase_data["Item ID"].unique())#returns count of times a unique item
print(count_unique_items_df)

#Average Price:
average_price = purchase_data["Price"].mean()
print(average_price)

#Number of Purchases:
count_purchases = len(purchase_data["Purchase ID"].unique())#returns count of times a unique item
print(count_purchases)

#Total Revenue:
total_revenue = purchase_data["Price"].sum()
print(total_revenue)

#Data Frame:
purchasing_analysis = pd.DataFrame({"Number of Unique Items": [count_unique_items_df], 
                                    "Average Price": [average_price], 
                                    "Number of Purchases": [count_purchases], 
                                    "Total Revenue": [total_revenue]})
purchasing_analysis

#Formatting:
#First convert columns to float then Format to go to two decimal places, include a dollar sign, and use comma notation
purchasing_analysis["Average Price"] = purchasing_analysis["Average Price"].astype(float).map(
    "${:,.2f}".format)
purchasing_analysis["Total Revenue"] = purchasing_analysis["Total Revenue"].astype(float).map(
    "${:,.2f}".format)
purchasing_analysis


##GENDER DEMOGRAPHICS
#Limit Data for information needed for Analysis:
limited_df = purchase_data.loc[:, ["SN", "Gender"]]
#print(limited_df)

# sorting by SN
limited_df.sort_values("SN", inplace = True)
 
# dropping ALL duplicate values
drop_dupes_df= limited_df.drop_duplicates(subset =["SN"],
                     keep = 'first')
#drop_dupes_df

#calc total: Total Count
grouped_by_gender = drop_dupes_df.groupby("Gender")
#grouped_by_gender.head()

#Calcs:
total_gender = grouped_by_gender.count()
total_gender
summed_gender = total_gender.sum()
summed_gender
percent_per_gender = (total_gender / summed_gender) *100
percent_per_gender

#DataFrame:
gender_purchasing_analysis = pd.DataFrame({"Total Count": [total_gender], 
                                    "Percentage of Players": [percent_per_gender]})

#Format:
#gender_purchasing_analysis["Percentage of Players"] = gender_purchasing_analysis["Percentage of Players"].astype(float).map("{:.2f}%".format)
gender_purchasing_analysis = gender_purchasing_analysis.sort_values(["Total Count"], ascending=False)

#Need to get the group by working*********************************************
#Need to fix the formatting*******************************