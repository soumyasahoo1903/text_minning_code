import os
import pandas as pd

# Directory path containing the Excel files
directory_path = '' ### give the directory path copy it form the folder 

# Initialize an empty list to store data from all Excel files
all_metabolites = []

# Loop through all files in the directory
for filename in os.listdir(directory_path):
    if filename.endswith('.xlsx'):  # Assuming the files have a .xlsx extension
        file_path = os.path.join(directory_path, filename)
        # Read the Excel file and extract the metabolites column into a DataFrame
        df = pd.read_excel(file_path)
        metabolites_column = df['Metabolites'] ### give the column name here which is common for all the files 
        # Append the metabolites from the current file to the list
        all_metabolites.append(metabolites_column)

# Concatenate all metabolite columns into one DataFrame
merged_metabolites_df = pd.concat(all_metabolites, ignore_index=True)

# Optionally, you can remove duplicates from the merged DataFrame
merged_metabolites_df.drop_duplicates(inplace=True)

# Save the merged DataFrame to a new Excel file
output_file_path = '--' #### give the output file path here 
merged_metabolites_df.to_excel(output_file_path, index=False)

print(f"Merged data saved to {output_file_path}")
