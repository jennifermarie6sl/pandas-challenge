import pandas as pd
import os

# File to Load (Remember to Change These)
file_to_load = os.path.join(".", "Desktop", "pandas-challenge", "HeroesOfPymoli", "Resources", "purchase_data.csv")

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)

#Unique players plus their count:
count_unique_players_df = len(purchase_data["SN"].unique())#returns count of times a unique item
print(count_unique_players_df)