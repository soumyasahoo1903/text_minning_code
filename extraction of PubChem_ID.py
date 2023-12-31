### code for extraction of PubChem_id
### no issues if the chunk size is not 100 the code still works and if requires then can increase as per the run speed of the code 

import pandas as pd
import requests

# Read the Excel file with metabolite names
df = pd.read_excel("F:/NISER internship/Text-minning/pubchem_id_description/metabolites(7179)(grp-2).xlsx")  # Replace 'metabolites.xlsx' with your file name

# Function to search for PubChem ID
def search_pubchem_id(metabolite_name):
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{metabolite_name}/cids/JSON"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'IdentifierList' in data:
            pubchem_id = data['IdentifierList']['CID'][0]
            return pubchem_id
    return None

# Chunk size for processing metabolite names
chunk_size = 100

# Get the total number of metabolite names
total_names = len(df)

# Process metabolite names in chunks
for i in range(0, total_names, chunk_size):
    # Extract the chunk of metabolite names
    chunk = df.iloc[i:i+chunk_size]

    # Add a new column 'PubChem ID' and search for PubChem ID for each metabolite name in the chunk
    chunk['PubChem ID'] = chunk['Metabolite'].apply(search_pubchem_id)

    # Save the updated chunk to an Excel file
    output_file = f"Metabolite_pubchem_ID_withIDs_{i+1}-{i+len(chunk)}.xlsx"
    chunk.to_excel(output_file, index=False)
    print(f"PubChem IDs extracted and saved to {output_file}")

print("All metabolite names processed.")
