import requests
from bs4 import BeautifulSoup

# URL of the website you want to scrape
url = 'https://www.summarycat.com'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the relevant elements containing the data you want to scrape
    # For example, if you want to scrape article titles (assuming they are in <h2> tags), you can do:
    article_titles = soup.find_all('title')

    # Extract the text from the article titles
    for title in article_titles:
        print(title.text)
else:
    print("Failed to fetch webpage:", response.status_code)
