#### merge articles and extract URL

import pandas as pd
import numpy as np
import re

# Read the Excel file
df = pd.read_excel("F:/NISER internship/text-mining for everyone's common metabolites/Sristi_di(500).xlsx")

# Convert NaN or float values to empty strings
df['Article Text'] = df['Article Text'].fillna('').astype(str)

# Extract URLs from the 'Article Text' column
df['urls'] = df['Article Text'].apply(lambda text: re.findall(r'(https?://\S+)', str(text)))

# Convert the list of URLs to a string
df['urls'] = df['urls'].apply(lambda urls: ', '.join(urls))

# Group by metabolite and concatenate functions
df_merged = df.groupby('Metabolite').agg({'Article Text': ', '.join, 'urls': ', '.join}).reset_index()

# Add count of merged rows
df_merged['Row Count'] = df.groupby('Metabolite').size().reset_index(name='Count')['Count']

# Save the merged data to a new Excel file
df_merged.to_excel("F:/NISER internship/text-mining for everyone's common metabolites/Sristi_di(500)merged_WKW.xlsx", index=False)
