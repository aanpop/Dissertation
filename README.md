**THIS DIRECTORY** is presented to store the data used in my dissertation. 
It has two main 'slots' of data: Qualitative data, stored in the 'Qualitative_Data' directory' ; and Quantitative data prepared in an excel file.





**Additionally**, there are two Python scripts. 


**1. (webscrapping.py)** to perform data extraction and web scraping tasks (especially to collect texts for qualitative analysis). Using a list of websites, the script extracts text content from each site and saves it into individual .txt files for further analysis or processing.

      **Features:**
      
      -Extracts text data from a list of websites.
      
      -Saves extracted content into separate .txt files for each website.
      
      -Efficient scraping using widely-used Python libraries.
      
      
      **Requirements**
      
      The script utilizes the following Python libraries:
      
      -pandas: for handling and processing data.      
      -requests: for making HTTP requests to retrieve webpage content.      
      -BeautifulSoup4: for parsing and extracting data from HTML and XML documents.
      
      
      **Usage**
      
      -Prepare an excel file containing a list of website URLs.
      -Run the Python script by providing the file as input.      
      -Extracted text from each website will be saved in a .txt file.


**2. (qualitive_content_analysis.py)** to run qualitative content analysis based on a predefined dictionary (concepts, operational definitions, and keyword variations based on the theoretical framework of neoliberal institutionalism) that guided the coding of text data.

      **Features:**
      -Deductive Conceptual Content Analysis: Performs content analysis based on a predefined dictionary of concepts and keywords.
      
      -Multi-format Text Processing: Reads and processes text from .txt, .docx, .md, .text, and .csv files within a zip archive.
      
      -Simple Sentence Splitting: Splits document content into sentences for granular analysis.
      
      -Case-Insensitive Keyword Matching: Identifies keywords within sentences regardless of case.
      
      -Contextual Information: For each flagged sentence, it captures the preceding and succeeding sentences as context.
      
      -Structured Outputs: Generates several CSV files:
      --analysis_sentences.csv: Detailed data for each sentence, including concept flags and matched keywords.
      --analysis_files.csv: A summary per file, including the total number of sentences and flagged sentences.
      --analysis_by_source.csv: Aggregates concept counts by document source type.
      --analysis_by_year.csv: Aggregates concept counts by year (extracted from filenames).
      
      -Example Sentences: Extracts and saves up to 10 unique example sentences per concept to a JSON file (examples_by_concept.json).
      
      -Robust File Reading: Includes basic error handling for unreadable files, reporting them in the summary.
      
      -Progress Reporting: Prints a concise summary of the analysis, including total files, sentences, and concept counts.
      
      **Requirements:**
      
      -Input Data: A .zip file containing the text documents (e.g., /content/text data.zip) must be available and its path correctly specified in the zip_path variable.
      -Python Libraries: The code relies on os, zipfile, re, json, traceback, collections, and pandas. These are standard libraries, but pandas might need installation (pip install pandas).
      
      **Usages:**
      Upload Zip File: Ensure your text data is packaged into a zip file and uploaded to your Colab environment (e.g., to /content/).
      -Specify zip_path: Update the zip_path variable in the code to point to the location of your uploaded zip file.
      -Define concept_keywords: Modify the concept_keywords dictionary to define the concepts you want to analyze and list the corresponding keywords and phrases for each concept.
      -Run the Code Cell: Execute the code cell (U29k8v8kQmMx).
      -Review Output: The code will print a summary to the console and save all detailed results (CSVs and JSON) in the /mnt/data/analysis_outputs directory, which you can then download or further analyze.
