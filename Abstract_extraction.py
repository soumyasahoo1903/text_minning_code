### extracts keywords for metabolite


import time
from Bio import Entrez, Medline
import pandas as pd
import openpyxl
from math import ceil
from http.client import IncompleteRead
from urllib.error import HTTPError

def search_metabolite_functions(query):
    Entrez.email = "soumyapooja39@gmail.com"
    attempt = 1
    while attempt <= 3:
        try:
            handle = Entrez.esearch(db='pubmed', sort='relevance', retmax='10', term=query)
            result = Entrez.read(handle)
            handle.close()
            return result["IdList"]
        except RuntimeError as e:
            print(f"RuntimeError occurred. Retrying... Attempt {attempt}")
            attempt += 1
            if attempt > 3:
                print(f"Maximum retries reached. Skipping.")
                return []

def fetch_article_text(id_list):
    Entrez.email = "soumyapooja39@gmail.com"
    articles = []
    for pmid in id_list:
        attempt = 1
        while attempt <= 3:
            try:
                handle = Entrez.efetch(db='pubmed', rettype='medline', retmode='text', id=pmid)
                record = Medline.read(handle)
                article_text = record.get('AB', 'N/A')
                if article_text != 'N/A':
                    article_text += f" [PMID: <a href='https://pubmed.ncbi.nlm.nih.gov/{pmid}' target='_blank'>{pmid}</a>]"
                articles.append(article_text)
                handle.close()
                break
            except (IncompleteRead, HTTPError) as e:
                print(f"Error occurred for PMID: {pmid}. Retrying... Attempt {attempt}")
                attempt += 1
                if attempt > 3:
                    print(f"Maximum retries reached for PMID: {pmid}. Skipping.")
    return articles

def read_metabolite_names_from_excel(file_path):
    df = pd.read_excel(file_path)
    metabolite_names = df['Metabolite'].tolist()
    return metabolite_names

def main():
    # Read metabolite names from an Excel file
    metabolite_names = read_metabolite_names_from_excel("F:/NISER internship/text-mining for everyone's common metabolites/Sristi_di(500).xlsx")

    # Set the chunk size
    chunk_size = 60

    # Calculate the number of chunks required
    num_chunks = ceil(len(metabolite_names) / chunk_size)

    # Create a new Excel file for results
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = 'Metabolite Functions'
    sheet.append(['Metabolite', 'Article Text'])

    total_start_time = time.time()  # Track total time taken

    # Iterate over each chunk of metabolite names
    for i in range(num_chunks):
        start_idx = i * chunk_size
        end_idx = (i + 1) * chunk_size

        # Get the current chunk of metabolite names
        metabolite_chunk = metabolite_names[start_idx:end_idx]

        chunk_start_time = time.time()  # Track time taken for each chunk

        # Iterate over each metabolite name in the current chunk
        for metabolite_name in metabolite_chunk:
            query = f'{metabolite_name}'
            # Search for the query
            id_list = search_metabolite_functions(query)

            # Fetch article text
            articles = fetch_article_text(id_list)

            # Save the metabolite name and article text in the Excel file
            for article in articles:
                sheet.append([metabolite_name, article])

        chunk_end_time = time.time()  # Track time taken for each chunk
        chunk_time = chunk_end_time - chunk_start_time
        print(f"Chunk {i+1} completed. Time taken: {chunk_time:.2f} seconds")

    total_end_time = time.time()  # Track total time taken
    total_time = total_end_time - total_start_time

    # Save the Excel file
    wb.save("F:/NISER internship/text-mining for everyone's common metabolites/Sristi_di(500).xlsx")

    print(f"Total time taken: {total_time:.2f} seconds")


if __name__ == '__main__':
    main()
    
    
    
