##remove /b----/b 
## and seperate the keywords into diffrent columns 


import pandas as pd

# Read the Excel file
df = pd.read_excel("F:/NISER internship/text-mining for everyone's common metabolites/Sristi_di(500)merged_WKW_updated_file.xlsx")


# Select the column containing the text
column_name = 'Matched Keywords'

# Remove '\b' and extract the words
df[column_name] = df[column_name].str.replace(r'\b', '')
df[column_name] = df[column_name].str.replace(r'\b', '', regex=False)

# Split the comma-separated values into different columns
df[column_name] = df[column_name].str.split(',')

# Create new columns for each separated value
new_columns = df[column_name].apply(pd.Series)
new_columns.columns = [f"{column_name}_{i+1}" for i in range(new_columns.shape[1])]

# Concatenate the new columns with the original DataFrame
df = pd.concat([df, new_columns], axis=1)

# Drop the original column
df.drop(column_name, axis=1, inplace=True)

# Save the modified DataFrame back to the Excel file
df.to_excel("F:/NISER internship/text-mining for everyone's common metabolites/Sristi_di(500)merged_WKW_updated_file.xlsx", index=False)
