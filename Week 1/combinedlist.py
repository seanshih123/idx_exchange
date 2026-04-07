import pandas as pd
import glob

# get all listing CSV files
files = glob.glob("/Users/seanshih/Desktop/IDX/Listings/*.csv")

# read and combine
dfs = [pd.read_csv(file, low_memory=False) for file in files]
combined = pd.concat(dfs, ignore_index=True)

# save output
combined.to_csv("CRMLSListed_All.csv", index=False)

print("Listings combined and saved as CRMLSListed_All.csv")