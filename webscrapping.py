import os
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Load the Excel file
file_path = r'C:\Users\ahmad\Desktop\Book1.xlsx'  # Replace with your Excel file path
sheet_name = 'Sheet1'  # Replace with your sheet name if different
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Ensure there's a column named 'URL' with the links
if 'URL' not in df.columns:
    raise ValueError("The Excel sheet must have a column named 'URL'")

# Create a directory to save the txt files
output_dir = 'scraped_articles'
os.makedirs(output_dir, exist_ok=True)


# Function to scrape article text from a given URL
def scrape_article_text(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the article text (adjust as necessary for the specific website)
        article = soup.find('article')
        if article:
            article_text = article.get_text(separator='\n', strip=True)
        else:
            article_text = "No article content found"

        return article_text

    except requests.exceptions.RequestException as e:
        return f"Error fetching {url}: {str(e)}"


# Loop through each URL, scrape the article text, and save it to a .txt file
for index, row in df.iterrows():
    url = row['URL']

    # Debug print to ensure loop is iterating over all rows
    print(f"Processing URL {index + 1}: {url}")

    # Scrape the text from the URL
    article_text = scrape_article_text(url)

    # Define the file name for the .txt file
    file_name = f"article_{index + 1}.txt"
    file_path = os.path.join(output_dir, file_name)

    # Save the article text to a .txt file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(article_text)

    # Debug print to confirm file saving
    print(f"Saved: {file_name}")

print("Scraping completed. All articles are saved in the 'scraped_articles' directory.")
