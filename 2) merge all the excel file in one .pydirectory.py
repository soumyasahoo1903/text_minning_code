import os
import pandas as pd

# Directory path containing the Excel files
directory_path = 'F:/NISER internship/text-mining_common_ metabolites/New folder' ## folder path 

# Initialize an empty list to store data from all Excel files
all_data = []

# Loop through all files in the directory
for filename in os.listdir(directory_path):
    if filename.endswith('.xlsx'):  # Assuming the files have a .xlsx extension
        file_path = os.path.join(directory_path, filename)
        # Read the Excel file and append it to the list
        df = pd.read_excel(file_path)
        all_data.append(df)

# Concatenate all DataFrames into one DataFrame
merged_data_df = pd.concat(all_data, ignore_index=True)

# Optionally, you can remove duplicates from the merged DataFrame
merged_data_df.drop_duplicates(inplace=True)

# Save the merged DataFrame to a new Excel file
output_file_path = 'F:/NISER internship/text-mining_common_ metabolites/New folder/output_file.xlsx' ## give output excel file path where all the merged data will be saved 
merged_data_df.to_excel(output_file_path, index=False)

print(f"Merged data saved to {output_file_path}")
