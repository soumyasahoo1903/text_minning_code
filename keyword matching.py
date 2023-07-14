#### keyword matching
## if needs to add more keywords then add in this format in the Keyword section r"\bkeyword\b"


import pandas as pd
import re

# Read the Excel file
df = pd.read_excel("F:/NISER internship/text-mining for everyone's common metabolites/Sristi_di(500)merged_WKW.xlsx")


# List of keywords
keywords = [
    r"\bAdipose\b", r"\bAdipogenesis\b", r"\bDifferentiation\b", r"\bBrowning\b", r"\bBeiging\b",
    r"\bLipogenesis\b", r"\bAdipocyte\b", r"\bObesity\b", r"\bObese\b", r"\bLipid accumulation\b",
    r"\bLipolysis\b", r"\bWAT\b", r"\bBAT\b", r"\bFat accumulation\b", r"\bFat degradation\b",
    r"\bFat deposition\b", r"\bColitis\b", r"\bInflammatory Bowel Disease\b", r"\bIBD\b",
    r"\bInflammation\b", r"\bInflammatory response\b", r"\bPro-inflammation\b",
    r"\bAnti-inflammation\b", r"\bGut barrier integrity\b", r"\bGut permeability\b",
    r"\bColon cancer\b"
]

# Initialize a new column to store matched keywords
df['Matched Keywords'] = ""

# Iterate over each row
for index, row in df.iterrows():
    text = str(row['Article Text'])  # Replace 'Your Column Name' with the actual column name in your Excel file
    matched_keywords = [re.sub(r"\b", "", keyword) for keyword in keywords if re.search(keyword, text, flags=re.IGNORECASE)]
    if matched_keywords:
        df.at[index, 'Matched Keywords'] = ', '.join(matched_keywords)


# Save the updated DataFrame to a new Excel file
df.to_excel("F:/NISER internship/text-mining for everyone's common metabolites/Sristi_di(500)merged_WKW_updated_file.xlsx", index=False)
