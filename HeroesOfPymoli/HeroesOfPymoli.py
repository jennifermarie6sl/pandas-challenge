import pandas as pd
import os

# File to Load (Remember to Change These)
file_to_load = os.path.join(".", "Desktop", "pandas-challenge", "HeroesOfPymoli", "Resources", "purchase_data.csv")

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)

total_players = purchase_data["SN"].count() #counts total in column
print(total_players)