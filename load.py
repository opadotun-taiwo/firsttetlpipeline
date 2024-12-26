import pandas as pd
import os

def load(full_data, full_data_file_path, agg_data, agg_data_file_path):
  	# Save both DataFrames as csv files. Set index = False to drop the index columns
    full_data.to_csv(full_data_file_path, index = False)
    agg_data.to_csv(agg_data_file_path, index = False)

load(clean_data, "clean_data.csv", agg_data, "agg_data.csv")

def validation(file_path):
    # Write your code here
    file_exists = os.path.exists(file_path)
    if not file_exists:
        raise Exception(f"There is not file in this {file_path}")
    
validation("clean_data.csv")
validation("agg_data.csv")