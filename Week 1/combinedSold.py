import pandas as pd
import glob

# path to your listings folder
files = glob.glob("/Users/seanshih/Desktop/IDX/Sold/*.csv")

# read and combine all CSVs
dfs = [pd.read_csv(file, low_memory=False) for file in files]
combined = pd.concat(dfs, ignore_index=True)

# save combined file
combined.to_csv("/Users/seanshih/Desktop/IDX/CRMLS_Sold_All.csv", index=False)

print("Done. Listings combined.")